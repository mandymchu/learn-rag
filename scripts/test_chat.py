import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from openai import OpenAI
from learn_rag.config import OPENAI_API_KEY, OPENAI_BASE_URL, OPENAI_CHAT_MODEL

client = OpenAI(api_key=OPENAI_API_KEY, base_url=OPENAI_BASE_URL)
response = client.chat.completions.create(
    model = OPENAI_CHAT_MODEL,
    messages =  [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain RAG in one sentence."},
    ],
    temperature = 0.1,
)

print(response.choices)
print(response.choices[0].message.content)
# output:
# [Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='RAG, or Retrieval-Augmented Generation, is a machine learning approach that combines information retrieval and natural language generation to enhance the generation of text by incorporating relevant external knowledge from a database or document collection.', refusal=None, role='assistant', annotations=[], audio=None, function_call=None, tool_calls=None))]
# RAG, or Retrieval-Augmented Generation, is a machine learning approach that combines information retrieval and natural language generation to enhance the generation of text by incorporating relevant external knowledge from a database or document collection.