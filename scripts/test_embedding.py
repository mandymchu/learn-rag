import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from learn_rag.embeddings import OpenAIEmbeddingClient, cosine_similarity

client = OpenAIEmbeddingClient()
sentences = [
    "How do I install this project?",
    "How do I run this repo?",
    "What should I eat for dinner?",
]

vectots = client.embed_texts(sentences)
for i in range(len(sentences)):
    for j in range(i+1, len(sentences)):
        sim = cosine_similarity(vectots[i], vectots[j])
        print(f"Similarity between '{sentences[i]}' and '{sentences[j]}': {sim:.4f}")

# Output:
# Similarity between 'How do I install this project?' and 'How do I run this repo?': 0.6408
# Similarity between 'How do I install this project?' and 'What should I eat for dinner?': 0.1654
# Similarity between 'How do I run this repo?' and 'What should I eat for dinner?': 0.1689
