from openai import OpenAI
from learn_rag.config import OPENAI_API_KEY, OPENAI_BASE_URL, OPENAI_EMBED_MODEL
import numpy as np


class OpenAIEmbeddingClient:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY, base_url=OPENAI_BASE_URL)

    def embed_text(self, text: str) -> list[float]:
        # call openai embeddings API for a single string
        # return a list of floats (the vector)
        response = self.client.embeddings.create(model=OPENAI_EMBED_MODEL, input=text)
        # response.data is a list — one item per input string. 
        # Since we passed a single string, we take [0]. .embedding is the vector as a list[float].
        return response.data[0].embedding

    def embed_texts(self, texts: list[str]) -> list[list[float]]:
        # embed multiple strings at once, returns a list of vectors
        # more efficient: 1 API call for multiple strings
        response = self.client.embeddings.create(model=OPENAI_EMBED_MODEL, input=texts)
        return [item.embedding for item in response.data]
    

def cosine_similarity(vector1: list[float], vector2: list[float]) -> float:
    # measure similarity between two vectors
    # returns a float between -1 and 1
    if np.linalg.norm(vector1) == 0 or np.linalg.norm(vector2) == 0:
        return 0.0
    return np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))
