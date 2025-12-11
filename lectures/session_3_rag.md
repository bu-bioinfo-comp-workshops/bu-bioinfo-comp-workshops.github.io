---
title: "Retrieval-Augmented Generation (RAG)"
sub_title: "Extending LLM capabilities with external knowledge"
author: "BU Bioinformatics Graduate Program"
options:
    end_slide_shorthand: true
---

Session 3: Retrieval-Augmented Generation
===

**Learning Objectives:**
- Understand when and why to use RAG
- Learn the RAG pipeline architecture
- Implement semantic search with embeddings
- Apply chunking strategies for scientific documents
- Build a simple RAG system for bioinformatics

---

Recap: The Context Window Problem
===

From Session 2, we know:
- Context windows are limited (e.g., 4K, 128K, 200K tokens)
- Everything must fit in *N* tokens
- Attention mechanism processes the entire context

**Question:** What if your knowledge base is millions of tokens?

---

Real-World Scenario
===

You want an LLM to answer questions about:
- Your lab's 500 protocols (∼2M tokens)
- 10,000 research papers (∼50M tokens)
- Genomic annotation databases (∼100M+ tokens)
- Your experiment notes from 5 years (∼500K tokens)

**Problem:** This won't fit in any context window

**Solution:** Retrieval-Augmented Generation (RAG)

---

What is RAG?
===

**Retrieval-Augmented Generation** = dynamically retrieve relevant information and add it to the context

**Key insight:** Don't put everything in context, just what's relevant to the current query

**Analogy:** Like having an index in a textbook - you don't read the whole book for every question

---

RAG Pipeline Overview
===

```
1. INDEXING (done once)
   Documents → Chunks → Embeddings → Vector Database

2. RETRIEVAL (per query)
   Query → Embedding → Search DB → Top-K chunks

3. AUGMENTATION (per query)
   Context = System + Retrieved chunks + Query

4. GENERATION (per query)
   LLM(Context) → Response
```

---

Why RAG Works
===

**Advantages:**
- Access to knowledge beyond training data
- Up-to-date information (update the index, not the model)
- Domain-specific knowledge (your protocols, data, papers)
- Traceable sources (know where answers come from)
- No fine-tuning required

**vs Fine-Tuning:**
- RAG: Dynamic, updatable, traceable
- Fine-tuning: Static, expensive, requires expertise

---

Embeddings Revisited
===

From the LLM Primer:
- **Embeddings** = vector representations of text
- Each token gets mapped to a high-dimensional vector
- Similar meanings → similar vectors

**New concept:** We can create embeddings for entire chunks of text, not just tokens

---

Semantic Similarity
===

Text embeddings capture **semantic meaning**

Example:
```
"BRCA1 mutation" 
"breast cancer susceptibility gene defect"
```

These have different words but similar embeddings because they mean similar things

**This enables semantic search** - find by meaning, not just keywords

---

The Indexing Phase (Step 1)
===

**Goal:** Prepare documents for efficient retrieval

Steps:
1. **Load documents** (PDFs, text files, databases, etc.)
2. **Split into chunks** (more on this next)
3. **Generate embeddings** for each chunk
4. **Store in vector database** (specialized DB for similarity search)

**Done once** (or when documents change)

---

Document Chunking
===

**Why chunk?**
- Embeddings work best on coherent units of meaning
- Retrieval precision (return specific relevant parts, not whole docs)
- Context window limits (even retrieved text must fit)

**Chunk size tradeoff:**
- Too small: Loss of context, fragmented information
- Too large: Less precise retrieval, more noise

**Typical sizes:** 200-1000 tokens per chunk with 10-20% overlap

---

Chunking Strategies
===

**1. Fixed-size chunks**
- Split every *N* characters/tokens
- Simple but may break mid-sentence/concept

**2. Sentence-based**
- Split on sentence boundaries
- More coherent but variable size

**3. Semantic chunks**
- Split on topic changes
- Best coherence but computationally expensive

**4. Structure-based** (for scientific papers)
- Split by section (Abstract, Methods, Results, etc.)
- Preserves logical organization

---

Chunking for Scientific Papers
===

Recommended approach:
```python
chunks = [
    {"section": "Abstract", "text": "...", "metadata": {...}},
    {"section": "Introduction", "text": "...", "metadata": {...}},
    {"section": "Methods", "text": "...", "metadata": {...}},
    {"section": "Results", "text": "...", "metadata": {...}},
    {"section": "Discussion", "text": "...", "metadata": {...}}
]
```

**Benefit:** Can prioritize sections by query type
- "How was this done?" → Methods
- "What did they find?" → Results

---

Vector Databases
===

**Regular database:** Exact match queries
```sql
SELECT * FROM papers WHERE title = "BRCA1 mutations"
```

**Vector database:** Similarity queries
```python
results = db.similarity_search(
    query_embedding,
    top_k=5
)
```

**Popular options:** ChromaDB, Pinecone, Weaviate, FAISS, Qdrant

---

The Retrieval Phase (Step 2)
===

For each query:

1. **Convert query to embedding** (same model as indexing)
2. **Search vector DB** for most similar chunks
3. **Rank by similarity score** (cosine similarity, dot product)
4. **Return top-K chunks** (typically K=3-10)

**Fast:** Optimized for high-dimensional similarity search

---

Similarity Metrics
===

How to measure "closeness" of vectors?

**Cosine similarity:** Angle between vectors
- Range: -1 to 1 (1 = identical)
- Most common for text

**Euclidean distance:** Geometric distance
- Range: 0 to ∞ (0 = identical)
- Sensitive to magnitude

**Dot product:** Direct vector multiplication
- Combines angle and magnitude

---

The Augmentation Phase (Step 3)
===

Build the context for the LLM:

```python
context = f"""
System: You are an expert bioinformatician. Answer based on 
the provided documents. Cite sources.

Retrieved Information:
{retrieved_chunk_1}

{retrieved_chunk_2}

{retrieved_chunk_3}

User Query: {user_question}
"""
```

---

The Generation Phase (Step 4)
===

Pass augmented context to LLM:

```python
response = completion(
    model="anthropic/claude-sonnet-4-20250514",
    messages=[{"role": "user", "content": context}]
)
```

The LLM generates answer based on:
- Its training knowledge
- **+ Retrieved specific information**

---

RAG vs Context Stuffing
===

**Context Stuffing:** Put all documents in context
- Limited by context window
- Expensive (all tokens processed)
- Attention spread across irrelevant info

**RAG:** Retrieve only relevant parts
- Scalable (millions of documents)
- Cheaper (only process relevant chunks)
- Focused attention on pertinent information

---

Retrieval Quality Matters
===

**The RAG Bottleneck:**

If retrieval fails to find relevant chunks, the LLM can't help

**Common issues:**
- Query-document vocabulary mismatch
- Chunk boundaries split important info
- Top-K too small (missed relevant docs)
- Top-K too large (noise dilutes signal)

**Solution:** Hybrid retrieval strategies

---

Hybrid Retrieval
===

**Semantic search alone** may miss exact keyword matches

**Keyword search alone** may miss semantic matches

**Hybrid approach:**
1. Semantic search (embedding similarity)
2. **+** Keyword search (BM25, TF-IDF)
3. Combine and rerank results

**Best of both worlds**

---

Reranking
===

**Problem:** Initial retrieval may have noise in top-K

**Solution:** Reranking step

1. Retrieve top-20 candidates (broad net)
2. **Rerank** using more sophisticated model
3. Take top-5 for context

**Reranker:** Specialized model trained to score query-document relevance

---

Metadata Filtering
===

**Enhance retrieval** with structured filters:

```python
results = db.similarity_search(
    query_embedding,
    filter={
        "organism": "Homo sapiens",
        "year": {"$gte": 2020},
        "journal": "Nature Genetics"
    },
    top_k=5
)
```

**Combines** semantic search with traditional filters

---

RAG in Bioinformatics: Use Cases
===

**1. Protocol search**
- "How do we extract RNA from tissue samples?"
- Retrieve from lab protocol database

**2. Literature review**
- "What's known about APOE variants and Alzheimer's?"
- Search thousands of papers

**3. Annotation lookup**
- "What pathways is EGFR involved in?"
- Query curated databases

**4. Experiment notes**
- "When did we last run sample XYZ?"
- Search lab notebooks

---

RAG Limitations
===

**1. Retrieval accuracy**
- Garbage in, garbage out
- Missed relevant docs = wrong answers

**2. Chunk boundary issues**
- Important info split across chunks
- May need larger chunks or overlap

**3. Conflicting information**
- Retrieved chunks may contradict
- LLM must reconcile (not always successful)

**4. Computational cost**
- Embedding generation
- Vector search overhead

---

When NOT to Use RAG
===

**Skip RAG when:**
- Information fits comfortably in context window
- General knowledge questions (LLM already knows)
- Real-time data needs (use tools/APIs instead - Session 3)
- Highly structured queries (use databases directly)

**Use RAG when:**
- Large knowledge base (beyond context limits)
- Domain-specific information
- Frequently updated content
- Need source attribution

---

RAG vs Fine-Tuning vs Prompting
===

**Prompting:** 
- Knowledge in context
- Best for: Task formatting, examples

**RAG:**
- Knowledge retrieved externally
- Best for: Large/updating knowledge bases

**Fine-Tuning:**
- Knowledge in model weights
- Best for: Behavior patterns, style, domain expertise

**Often combined** for best results

---

Practical Demo Overview
===

We'll build two RAG systems:

1. **Paper Q&A:** Query a collection of genomics papers
2. **Protocol Assistant:** Search lab protocols and methods

We'll see:
- Document loading and chunking
- Embedding generation
- Vector database setup
- Query and retrieval
- Answer generation with sources

---

Demo 1: Paper Q&A System
===

**System components:**
- ChromaDB for vector storage
- Sentence-transformers for embeddings
- LiteLLM for generation
- Sample genomics papers

**Flow:**
1. Load papers → chunk by section
2. Generate embeddings → store in ChromaDB
3. Query: "What sequencing methods were used?"
4. Retrieve relevant chunks
5. Generate answer with citations

---

Demo 2: Protocol Search
===

**System components:**
- Structured protocol documents
- Metadata (author, date, tags)
- Hybrid search (semantic + metadata filters)

**Flow:**
1. Index protocols with metadata
2. Query: "RNA extraction from blood samples"
3. Filter: protocols from last 2 years
4. Retrieve and generate step-by-step answer

---

Key Takeaways
===

1. **RAG extends LLM knowledge** beyond training and context limits
2. **Pipeline:** Index → Retrieve → Augment → Generate
3. **Embeddings enable semantic search** (meaning, not just keywords)
4. **Chunking strategy matters** for retrieval quality
5. **Vector databases** make similarity search fast
6. **Hybrid approaches** (semantic + keyword) often work best
7. **RAG ≠ perfect** - retrieval quality is critical

---

Theory ↔ Practice Connections
===

**Theory:** Embeddings capture semantic meaning in vector space

**Practice:** Similar concepts cluster together, enabling semantic search

---

**Theory:** Attention mechanism processes all context tokens

**Practice:** Only include relevant retrieved chunks to focus attention

---

**Theory:** Context windows have hard token limits

**Practice:** RAG circumvents limits by selective retrieval

---

Looking Ahead: Session 4
===

**Next topic:** Tool Use & Function Calling

**The problem we'll solve:**

RAG retrieves static documents. What about dynamic information?
- Database queries
- API calls  
- Running computations
- Accessing real-time data

**Solution:** Give LLMs the ability to use tools

---

Resources
===

**Libraries:**
- LlamaIndex - https://www.llamaindex.ai/
- LangChain - https://www.langchain.com/
- ChromaDB - https://www.trychroma.com/
- Sentence-Transformers - https://www.sbert.net/

**Papers:**
- "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" (Lewis et al., 2020)
- "REALM: Retrieval-Augmented Language Model Pre-Training" (Guu et al., 2020)

**Demo code:** `lectures/demos/session_3/`

---

Questions?
===

Next session: **Tool Use & Function Calling**
