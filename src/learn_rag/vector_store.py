from learn_rag.embeddings import cosine_similarity, OpenAIEmbeddingClient
import json


class VectorStore():
    def __init__(self) -> None:
        self.entries = []
        self.client = OpenAIEmbeddingClient()

    def add(self, text: str, source_path: str) -> None:
        embedding = self.client.embed_text(text)
        metadata = {"source": source_path, "chunk_index": len(self.entries)}
        self.entries.append({"text": text, "embedding": embedding, "metadata": metadata})

    def search(self, query: str, top_k: int = 3) -> list[dict]:
        similarity_list = []
        query_embedding = self.client.embed_text(query)
        for entry in self.entries:
            similarity_list.append({**entry, "similarity": cosine_similarity(query_embedding, entry["embedding"])})
        sorted_entries = sorted(similarity_list, key=lambda x: x["similarity"], reverse=True)
        return sorted_entries[:top_k]

    def save(self, file_path: str) -> None:
        with open(file_path, "w") as f:
            json.dump(self.entries, f)
    
    def load(self, file_path: str) -> None:
        with open(file_path, "r") as f:
            self.entries = json.load(f)
        