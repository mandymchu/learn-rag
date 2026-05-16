import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from learn_rag.rag_pipeline import rag_ask

question = sys.argv[1] if len(sys.argv) > 1 else "What is RAG?"
answer, sources = rag_ask(question)
print(f"Question: {question}\n")
print(f"Answer: {answer}\n")
print("Sources:")
for source in sources:
    print(f"- {source}")

# output format:
# Answer: RAG combines retrieval with generation...
# Sources:
# - TinyRAG/readme.md (chunk 2, similarity: 0.84)
# - TinyAgent/readme.md (chunk 0, similarity: 0.71)

# Output example:
# % python scripts/ask.py "What is RAG? How can I learn RAG by this project?"
# Question: What is RAG? How can I learn RAG by this project?

# Answer: RAG stands for Retrieval-Augmented Generation. It is a technology that combines the capabilities of 
# large language models with external knowledge bases to improve the accuracy and relevance of generated content. 
# RAG works by first retrieving relevant information from a wide range of documents before generating answers, 
# which helps alleviate issues like "hallucinations" (misleading or incorrect information) and enhances the model's ability to provide up-to-date and traceable content.

# You can learn RAG through the TinyRAG project by following the step-by-step implementation guide provided in the project. 
# The TinyRAG project simplifies the core functionalities of RAG, focusing on Retrieval and Generation, which will help you understand the principles and 
# implementation of RAG models. The project includes explanations of necessary implementation steps and encourages you to think critically 
# about how to complete the implementation, allowing for a deeper understanding of RAG technology.

# Sources:
# - tinyrag_readme.md (chunk 51, similarity: 0.65)
# - tinyrag_readme.md (chunk 52, similarity: 0.65)
# - Building TinyCodeRAG Step-by-Step_ A Lightweight Code Knowledge Base Solution _ CodeMLS.pdf (chunk 11, similarity: 0.61)
# - tiny_graph_rag_readme.md (chunk 74, similarity: 0.58)
# - tiny_graph_rag_readme.md (chunk 73, similarity: 0.55)