# Phase 6 — Full RAG Pipeline + Sources

# 1. Load the vector store from disk
# 2. Embed the query
# 3. Search for top-k relevant chunks
# 4. Build a prompt with retrieved context injected
# 5. Call the LLM
# 6. Return answer + sources (file, chunk_index, similarity score)

import os
from openai import OpenAI
from learn_rag.vector_store import VectorStore
from learn_rag.config import OPENAI_API_KEY, OPENAI_BASE_URL, OPENAI_CHAT_MODEL


def rag_ask(question, top_k=5, loaded_vector_store=None):
    # 1. Load the vector store from disk
    if not loaded_vector_store:
        PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        vector_store_path = os.path.join(PROJECT_ROOT, "scripts", "test_results", "vector_store.json")
        vector_store = VectorStore()
        vector_store.load(vector_store_path)
    else:
        vector_store = loaded_vector_store

    # 2. Embed the query and search for top-k relevant chunks
    relevant_chunks = vector_store.search(question, top_k=top_k)

    # 3. Build a prompt with retrieved context injected
    # You are a helpful assistant. Answer the question based only on the context below.
    # Context:
    # {context}   # {context} is filled with the retrieved chunks' text, concatenated together.
    # Question: {question}
    # Answer:

    context =""
    for chunk in relevant_chunks:
        context += chunk["text"] + "\n"
    prompt = f"You are a helpful assistant. Answer the question based only on the context below.\nContext:\n{context}"
    
    # 4. Call the LLM
    client = OpenAI(api_key=OPENAI_API_KEY, base_url=OPENAI_BASE_URL)
    response = client.chat.completions.create(
        model = OPENAI_CHAT_MODEL,
        messages =  [
            {"role": "system", "content": prompt},
            {"role": "user", "content": question},
        ],
        temperature = 0.1,
    )

    # 5. Return answer + sources (file, chunk_index, similarity score)
    # output format:
    # Answer: RAG combines retrieval with generation...
    # Sources:
    # - TinyRAG/readme.md (chunk 2, similarity: 0.84)
    # - TinyAgent/readme.md (chunk 0, similarity: 0.71)
    answer = response.choices[0].message.content
    sources = []
    for chunk in relevant_chunks:
        source_info = f"{os.path.basename(chunk['metadata']['source'])} (chunk {chunk['metadata']['chunk_index']}, similarity: {chunk['similarity']:.2f})"
        sources.append(source_info)
    return answer, sources


    
    
