# Session 2: Retrieval-Augmented Generation (RAG) - Demo Code

This directory contains demonstrations for building RAG systems in bioinformatics.

## Setup

### Prerequisites
```bash
python -m venv .venv
source .venv/bin/activate
pip install litellm python-dotenv chromadb sentence-transformers
```

### API Key Configuration
```bash
# For OpenAI embeddings (or use open-source alternatives)
export OPENAI_API_KEY=sk-your-key-here
export ANTHROPIC_API_KEY=sk-ant-your-key-here
```

## Demos

### Demo 1: Paper Q&A System
**File:** `demo_1_paper_qa.py`

**What it demonstrates:**
- Document chunking by sections
- Embedding generation and storage
- Vector database (ChromaDB) usage
- Semantic search and retrieval
- Context augmentation
- Answer generation with citations
- Metadata filtering

**Run:**
```bash
python demo_1_paper_qa.py
```

**Key concepts:**
- RAG pipeline: Index → Retrieve → Augment → Generate
- Semantic similarity search
- Source attribution

---

## RAG Pipeline Steps

### 1. Indexing (Done Once)
```python
# Load documents
documents = load_papers()

# Chunk documents
chunks = chunk_by_section(documents)

# Generate embeddings
embeddings = embed_chunks(chunks)

# Store in vector DB
vector_db.add(chunks, embeddings, metadata)
```

### 2. Retrieval (Per Query)
```python
# Convert query to embedding
query_embedding = embed(user_question)

# Search for similar chunks
relevant_chunks = vector_db.search(
    query_embedding,
    top_k=5
)
```

### 3. Augmentation (Per Query)
```python
# Build context
context = f"""
System prompt: ...

Retrieved information:
{relevant_chunk_1}
{relevant_chunk_2}
{relevant_chunk_3}

Question: {user_question}
"""
```

### 4. Generation (Per Query)
```python
# Generate answer
answer = llm.complete(context)
```

---

## Chunking Strategies

### For Scientific Papers
```python
def chunk_by_section(paper):
    """Split paper into logical sections."""
    return [
        {"section": "abstract", "text": paper.abstract},
        {"section": "methods", "text": paper.methods},
        {"section": "results", "text": paper.results},
        {"section": "discussion", "text": paper.discussion}
    ]
```

**Advantages:**
- Preserves logical structure
- Section-specific retrieval
- Better coherence

### For Protocols
```python
def chunk_protocol(protocol):
    """Chunk protocol by steps."""
    return [
        {"step": i, "text": step_text}
        for i, step_text in enumerate(protocol.steps)
    ]
```

---

## Embedding Models

### OpenAI (Proprietary)
```python
from litellm import embedding

response = embedding(
    model="text-embedding-ada-002",
    input=["text to embed"]
)
```

### Open Source Alternative
```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(["text to embed"])
```

**Recommendation:** Use open-source models for sensitive data

---

## Vector Databases Comparison

| Database | Pros | Cons | Best For |
|----------|------|------|----------|
| ChromaDB | Easy to use, local | Limited scale | Development, small projects |
| FAISS | Fast, Facebook-backed | No metadata filtering | Large-scale similarity search |
| Pinecone | Managed, scalable | Requires account, cost | Production systems |
| Qdrant | Full-featured, fast | More complex setup | Production with filtering needs |

---

## Troubleshooting

**Poor retrieval quality:**
- Try different embedding models
- Adjust chunk size (larger for more context, smaller for precision)
- Increase top_k (retrieve more candidates)
- Add overlap between chunks
- Use hybrid search (semantic + keyword)

**Contradictory answers:**
- Implement reranking step
- Add confidence scores
- Show sources to users
- Use larger top_k and let LLM reconcile

**Slow performance:**
- Use approximate nearest neighbor algorithms
- Reduce embedding dimensions
- Batch process queries
- Cache frequent queries

---

## Advanced Techniques

### Hybrid Search
Combine semantic and keyword search:
```python
# Semantic results
semantic = vector_db.search(query_embedding, top_k=10)

# Keyword results (BM25)
keyword = bm25_search(query_text, top_k=10)

# Merge and rerank
final = rerank(semantic + keyword, query)[:5]
```

### Reranking
Use cross-encoder for better relevance:
```python
from sentence_transformers import CrossEncoder

reranker = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

# Score query-document pairs
scores = reranker.predict([
    (query, doc) for doc in candidates
])

# Sort by score
ranked = sorted(zip(candidates, scores), key=lambda x: x[1], reverse=True)
```

### Query Expansion
Improve recall by expanding queries:
```python
# Generate related queries
expanded = llm.complete(
    f"Generate 3 alternative phrasings of: {query}"
)

# Search with all variants
results = [
    vector_db.search(q) for q in [query] + expanded
]

# Merge results
final_results = deduplicate_and_rank(results)
```

---

## Exercises

### Exercise 1: Protocol RAG
Build a RAG system for your lab's protocols:
- Load protocol documents
- Chunk by procedure steps
- Add metadata (author, date, equipment)
- Implement search with filtering

### Exercise 2: Multi-Modal RAG
Extend the paper Q&A to handle figures:
- Extract figure captions
- Use CLIP for image embeddings
- Retrieve relevant figures for questions
- Generate answers referencing both text and figures

### Exercise 3: Hybrid Search
Implement hybrid retrieval:
- Add BM25 keyword search
- Combine with semantic search
- Compare results quality

---

## Resources

**Libraries:**
- ChromaDB: https://www.trychroma.com/
- LlamaIndex: https://www.llamaindex.ai/
- LangChain: https://www.langchain.com/
- Sentence-Transformers: https://www.sbert.net/

**Papers:**
- "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" (Lewis et al., 2020)
- "Dense Passage Retrieval for Open-Domain Question Answering" (Karpukhin et al., 2020)

**Embeddings:**
- Sentence-BERT paper: https://arxiv.org/abs/1908.10084
- MTEB Leaderboard: https://huggingface.co/spaces/mteb/leaderboard
