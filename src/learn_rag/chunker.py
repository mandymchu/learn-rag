import os
import fitz  # PyMuPDF
from docx import Document

SUPPORTED_EXTENSIONS = {'.md', '.txt', '.py', '.pdf', '.docx'}

def _read_file(file_path: str, ext: str) -> str:
    if ext in {'.md', '.txt', '.py'}:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    elif ext == '.pdf':
        doc = fitz.open(file_path)
        return "\n".join(page.get_text() for page in doc)
    elif ext == '.docx':
        doc = Document(file_path)
        return "\n".join(para.text for para in doc.paragraphs)

# The function walks the directory and finds all supported files inside it itself.
# supporting loading from .txt, .md, .py, .pdf, .docx
def load_documents(directory: str) -> list[dict]:
    # returns [{"text": "...", "source": "path/to/file.md"}, ...]
    documents = []
    for root, _, files in os.walk(directory):
        for filename in files:
            ext = os.path.splitext(filename)[1].lower()
            if ext not in SUPPORTED_EXTENSIONS:
                print(f"filename {filename} has unsupported extension {ext}, skipping.")
                continue
            file_path = os.path.join(root, filename)
            text = _read_file(file_path, ext)
            if text:
                documents.append({"text": text, "source": file_path})
    return documents

def chunk_text(text: str, source: str, chunk_size: int = 500, overlap: int = 50) -> list[dict]:
    # Splits a full document text into overlapping chunks.
    # Each chunk advances by (chunk_size - overlap) characters,
    # so adjacent chunks share `overlap` characters at their boundary.
    # Example: chunk_size=500, overlap=50 → chunk 0 covers [0:500], chunk 1 covers [450:950], etc.
    # returns [{"chunk_index": 0, "text": "...", "source": "..."}, ...]
    chunks = []
    start = 0
    chunk_index = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append({"text": chunk, "source": source, "chunk_index": chunk_index})
        start += chunk_size - overlap
        chunk_index += 1
    return chunks

def load_and_chunk(directory: str, chunk_size: int = 500, overlap: int = 50) -> list[dict]:
    all_chunks = []
    documents = load_documents(directory)
    for doc in documents:
        chunks = chunk_text(doc["text"], doc["source"], chunk_size, overlap)
        all_chunks.extend(chunks)
    return all_chunks
