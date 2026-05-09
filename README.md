# learn-rag

A from-scratch OpenAI-based RAG system, built for learning.

Reference: [TinyCodeBase/RAG](https://github.com/codemilestones/TinyCodeBase/tree/master/RAG)

---

## Final Workflow

```
Local documents / code files
  -> load files
  -> split into chunks
  -> create embeddings
  -> store vectors locally
  -> ask a question
  -> retrieve relevant chunks
  -> send context to OpenAI LLM
  -> generate grounded answer
```

**RAG** — Retrieval-Augmented Generation 
---

## Project Structure

```
learn-rag/
  src/
    learn_rag/
      __init__.py
      config.py          # env vars and settings
      llm.py             # OpenAI chat client
      embeddings.py      # OpenAI embedding client
      chunker.py         # text and code chunking
      vector_store.py    # store, search, persist vectors
      rag_pipeline.py    # end-to-end RAG pipeline
  scripts/
    test_chat.py         # Phase 1: verify OpenAI setup
    test_embedding.py    # Phase 2: verify embeddings
    ingest.py            # Phase 5: build the vector index
    ask.py               # Phase 6: query the RAG system
  examples/
    sample_docs/         # sample markdown files for testing
  storage/               # auto-generated, git-ignored
    vector_store.json
  .env.example
  requirements.txt
```

---

## Roadmap

### Phase 1 — Environment + OpenAI Chat
**Files:** `config.py`, `scripts/test_chat.py`

- Load API keys from `.env` using `python-dotenv`
- Call `chat.completions.create()` with a simple question
- Understand `messages` format: `system` / `user` / `assistant`

**Key concept:** API key / 密钥 — never hardcode, always load from `.env`

✅ `python scripts/test_chat.py` answers a simple question

---

### Phase 2 — Embedding Client
**File:** `embeddings.py`, `scripts/test_embedding.py`

- Call `embeddings.create()` to convert text into a vector
- Implement `cosine_similarity()` to measure how similar two vectors are
- Verify: two similar sentences score higher than two unrelated ones

**Key concept:** Embedding  — text → list of numbers; similar meaning = similar direction in vector space

**Key concept:** Cosine similarity  — measures angle between two vectors; closer to 1 = more similar

✅ `python scripts/test_embedding.py` shows similarity scores

---

### Phase 3 — Vector Store
**File:** `vector_store.py`

- Store chunks + their embeddings in memory
- `save()` / `load()` to persist as JSON — avoid re-embedding on every run
- `search()` returns top-k most similar chunks for a given query

**Key concept:** Vector store — stores text chunks and embeddings, retrieves the most relevant ones at query time

✅ Add 5 manual entries → query → returns top 3 relevant chunks

---

### Phase 4 — Document Loader + Text Chunker
**File:** `chunker.py`

- Read `.md`, `.txt`, `.py` files from a directory
- Split long text into overlapping chunks by character count
- Attach metadata: source file path, chunk index

**Key concept:** Chunking  — split long docs into small pieces; LLMs and embedding models have token limits

**Key concept:** Overlap  — each chunk repeats the tail of the previous one, so context is not cut off at boundaries

✅ A 2,000-char document → several chunks, each with source metadata

---

### Phase 5 — Ingestion Pipeline
**File:** `scripts/ingest.py`

Wire together: load → chunk → embed → save

**Key concept:** Ingestion — the offline process of preparing documents for retrieval

✅ `python scripts/ingest.py examples/sample_docs` outputs:
```
Loaded 3 files
Created 12 chunks
Embedded 12 chunks
Saved to storage/vector_store.json
```

---

### Phase 6 — Full RAG Pipeline + Sources
**File:** `rag_pipeline.py`, `scripts/ask.py`

- Embed the question → search vector store → build prompt with retrieved context → call LLM
- Return answer + sources (file, chunk index, similarity score) from day one

**Key concept:** Context injection  — fill retrieved chunks into `{context}` in the prompt template

**Key concept:** Grounded answer — the answer is based on retrieved evidence, not the model's general memory

✅ `python scripts/ask.py "What is RAG?"` returns answer + sources

---

### Phase 7 — Code-Aware Chunking
**File:** update `chunker.py`

- Simple strategy: split Python files around `def` / `class` boundaries
- Add `file_type` to metadata
- Ingest the `learn-rag` repo itself and ask code questions

**Key concept:** Code RAG  — retrieve relevant code snippets so the model can explain a codebase

✅ `python scripts/ask.py "Where is the vector store implemented?"`

---

### Phase 8 — Evaluation + Comparison
**File:** manual test cases

- Write test cases with expected source files
- Check whether retrieval returns the right chunks
- Compare with [TinyCodeBase/RAG](https://github.com/codemilestones/TinyCodeBase/tree/master/RAG) file by file

**Key concept:** Evaluation / 评估 — verify retrieval quality before adding new features

✅ Test cases pass → compare design decisions with TinyCodeBase

---

## Commit Roadmap

```
01-scaffold-project
02-openai-chat-client
03-embedding-client
04-vector-store-with-search
05-document-loader-and-chunker
06-ingest-script
07-rag-pipeline-with-sources
08-code-aware-chunking
09-evaluation-and-comparison
```

---

## Study Plan (12 days)

| Day | Goal |
|-----|------|
| 1 | Scaffold + OpenAI chat working |
| 2 | Embeddings + similarity experiment |
| 3 | Vector store: add, save, load, search |
| 4 | Document loader + text chunker |
| 5 | Ingest sample docs, verify storage output |
| 6 | RAG pipeline first version |
| 7 | Add sources + scores, improve prompt |
| 8 | Manual evaluation — does it actually work? |
| 9 | Code-aware chunking (simple) |
| 10 | Ingest learn-rag repo itself, ask code questions |
| 11 | Compare with TinyCodeBase file by file |
| 12 | Clean up, write notes, final commit |

---

## Setup

```bash
cp .env.example .env
# fill in your API key in .env

pip install -r requirements.txt
python scripts/test_chat.py
```
