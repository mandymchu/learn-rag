# Verification plan (`scripts/test_vector_store.py`)

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import json
from learn_rag.vector_store import VectorStore


# 1. Create a `VectorStore`
vector_store = VectorStore()

# 2. Manually add 5 entries with their embeddings (use `OpenAIEmbeddingClient`)
entries = [ "This is a test document for phase 3 vectore store. The chunks are manually created for testing purpose.",
            "It is an entry for vector store testing purpose. The content is about RAG system and vector search. It has 8 phases in total, and we are currently in phase 3.",
            "How does vector store work in RAG system? ",
            "What is the progress of this project so far? How many phases have been completed?",
            "How many phases are there in this project? What is the focus of each phase?" 
]
for entry in entries:
    vector_store.add(entry, "test_source")

# 3. Query with a question
query = "What is the current phase of the project? And what is the goal of this phase?"

# 4. Assert the top results are the relevant ones
results = vector_store.search(query, top_k=3)

# # 5. Save to `./test_results/vector_store.json`
result_folder = os.path.join(os.path.dirname(__file__), "test_results")
os.makedirs(result_folder, exist_ok=True)
vector_store.save(os.path.join(result_folder, "vector_store.json"))

# reload, search again — same results
vector_store.load(os.path.join(result_folder, "vector_store.json"))
results_after_reload = vector_store.search(query, top_k=3)
assert results == results_after_reload, "Results after reload should be the same as before"

# print out the results
print(f"Query:, {query}\n")
print("Top results:")
for res in results:
    print(f"Text: {res['text']}\n   Metadata: {res['metadata']}\n")

### output:
# Query:, What is the current phase of the project? And what is the goal of this phase?

# Top results:
# Text: How many phases are there in this project? What is the focus of each phase?
#    Metadata: {'source': 'test_source', 'chunk_index': 4}

# Text: What is the progress of this project so far? How many phases have been completed?
#    Metadata: {'source': 'test_source', 'chunk_index': 3}

# Text: It is an entry for vector store testing purpose. The content is about RAG system and vector search. It has 8 phases in total, and we are currently in phase 3.
#    Metadata: {'source': 'test_source', 'chunk_index': 1}