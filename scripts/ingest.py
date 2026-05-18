import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from learn_rag.vector_store import VectorStore
from learn_rag.chunker import load_and_chunk    

if __name__ == "__main__":
    # 1. Load and chunk the documents
    # directory = os.path.join(os.path.dirname(__file__), "test_data", "sample_docs")
    directory = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "test_data", "sample_docs")
    chunks = load_and_chunk(directory)
    # [{"chunk_index": 0, "text": "chunk text...", "source": "..."}, ...]
    print(f"Loaded and chunked: {len(chunks)} chunks from {len(set(chunk['source'] for chunk in chunks))} files")

    # 2. Create a vector store and add chunks
    store = VectorStore()
    # [{"text": text, "embedding": embedding, "metadata": metadata}, ...]
    for chunk in chunks:
        store.add(chunk["text"], chunk["source"])
    print(f"Embedded and stored {len(chunks)} chunks")

    # 3. Save the vector store
    result_folder = os.path.join(os.path.dirname(__file__), "test_results")
    os.makedirs(result_folder, exist_ok=True)
    store.save(os.path.join(result_folder, "vector_store.json"))
    print(f"Saved to {os.path.join(result_folder, 'vector_store.json')}")

## test output:
# filename .DS_Store has unsupported extension , skipping.
# Loaded and chunked: 174 chunks from 8 files
# Embedded and stored 174 chunks
# Saved to xxx/scripts/test_results/vector_store.json