"""
Demo 1: Paper Q&A System using RAG

This demo builds a simple RAG system to answer questions about
genomics research papers.
"""

from litellm import completion, embedding
import chromadb
from chromadb.config import Settings
import dotenv
import os
from typing import List, Dict
import uuid

dotenv.load_dotenv()

print("=" * 80)
print("Demo 1: Building a Paper Q&A System with RAG")
print("=" * 80)

# ============================================================================
# Sample Papers (simulating parsed paper sections)
# ============================================================================

papers = [
    {
        "id": "paper1",
        "title": "Whole-genome sequencing in diverse populations",
        "authors": "Smith et al.",
        "year": 2023,
        "sections": {
            "abstract": """
            We performed whole-genome sequencing on 10,000 individuals from 
            diverse ancestral backgrounds to characterize genetic variation. 
            Using Illumina NovaSeq platforms, we achieved 30x coverage and 
            identified 150 million variants.
            """,
            "methods": """
            DNA extraction was performed using the Qiagen DNeasy Blood & Tissue Kit.
            Libraries were prepared using the Illumina DNA Prep kit with unique 
            dual indexes. Sequencing was performed on NovaSeq 6000 using S4 flow 
            cells with 2x150bp paired-end reads. Alignment to GRCh38 was done 
            with BWA-MEM, and variant calling used GATK HaplotypeCaller.
            """,
            "results": """
            We identified 150 million variants, including 12 million novel 
            variants not present in dbSNP. Population-specific variants were 
            enriched in understudied populations. The average individual carried 
            4.5 million variants, with 12,000 coding variants per genome.
            """,
            "discussion": """
            This study expands our understanding of human genetic diversity.
            The novel variants identified are predominantly in non-European 
            populations, highlighting the importance of diverse sequencing efforts.
            These data will improve clinical interpretation in underrepresented groups.
            """,
        },
    },
    {
        "id": "paper2",
        "title": "Long-read sequencing for structural variant detection",
        "authors": "Jones et al.",
        "year": 2023,
        "sections": {
            "abstract": """
            Structural variants (SVs) are challenging to detect with short-read 
            sequencing. We used PacBio HiFi long-read sequencing to characterize
            SVs in 500 genomes, identifying 25,000 SVs per individual, including
            many missed by short reads.
            """,
            "methods": """
            High molecular weight DNA was extracted using the Circulomics Nanobind 
            kit. SMRTbell libraries were prepared following PacBio's protocol. 
            Sequencing was performed on Sequel IIe using HiFi mode to generate 
            reads averaging 15kb at >99% accuracy. SV calling used pbsv and SVIM.
            """,
            "results": """
            Each genome contained an average of 25,000 SVs >50bp, including 
            deletions (45%), insertions (40%), and complex rearrangements (15%).
            Long reads detected 2x more SVs than short-read methods. Many SVs 
            were in medically relevant genes like HBA1, SMN1, and CYP2D6.
            """,
            "discussion": """
            Long-read sequencing is superior for comprehensive SV detection. The
            additional SVs identified have potential clinical relevance. We 
            recommend long-read sequencing for complete genome characterization,
            especially for diagnostic applications.
            """,
        },
    },
    {
        "id": "paper3",
        "title": "Single-cell RNA-seq reveals tumor heterogeneity",
        "authors": "Lee et al.",
        "year": 2024,
        "sections": {
            "abstract": """
            We used single-cell RNA-seq to profile 50,000 cells from breast cancer
            tumors. We identified 8 distinct cell populations and characterized
            their transcriptional profiles, revealing significant tumor heterogeneity.
            """,
            "methods": """
            Fresh tumor samples were dissociated using the Miltenyi Tumor 
            Dissociation Kit. Viable cells were sorted by FACS. Single-cell 
            libraries were prepared using 10x Genomics Chromium with v3.1 chemistry.
            Sequencing was performed on NovaSeq 6000. Analysis used Seurat and 
            scanpy pipelines for clustering and differential expression.
            """,
            "results": """
            We identified 8 cell clusters including cancer cells, immune cells,
            and stromal cells. Cancer cells showed two distinct transcriptional 
            states correlating with proliferation and invasion. CD8+ T cells were
            enriched in tumors with better prognosis. 2,500 genes showed 
            differential expression between clusters.
            """,
            "discussion": """
            Single-cell analysis reveals intratumoral heterogeneity not visible
            in bulk sequencing. The distinct cancer cell states suggest therapeutic
            vulnerabilities. Immune cell infiltration patterns correlate with 
            patient outcomes and may guide immunotherapy selection.
            """,
        },
    },
]

# ============================================================================
# Step 1: Create chunks from papers
# ============================================================================

print("\n--- Step 1: Chunking Papers ---\n")

chunks = []
for paper in papers:
    for section_name, section_text in paper["sections"].items():
        chunk = {
            "id": f"{paper['id']}_{section_name}",
            "text": section_text.strip(),
            "metadata": {
                "paper_id": paper["id"],
                "title": paper["title"],
                "authors": paper["authors"],
                "year": paper["year"],
                "section": section_name,
            },
        }
        chunks.append(chunk)

print(f"Created {len(chunks)} chunks from {len(papers)} papers")
print("\nExample chunk:")
print(f"ID: {chunks[0]['id']}")
print(f"Section: {chunks[0]['metadata']['section']}")
print(f"Text preview: {chunks[0]['text'][:100]}...")

input("\n[Press Enter to continue to Step 2: Embeddings...]")

# ============================================================================
# Step 2: Generate embeddings and store in ChromaDB
# ============================================================================

print("\n--- Step 2: Generating Embeddings & Storing in Vector DB ---\n")

# Initialize ChromaDB (in-memory for demo)
client = chromadb.Client(Settings(anonymized_telemetry=False, is_persistent=False))

# Create collection
collection = client.create_collection(
    name="genomics_papers", metadata={"description": "Genomics research papers"}
)

print("Generating embeddings for chunks...")

# For this demo, we'll use a simple embedding approach
# In production, use sentence-transformers or similar
for i, chunk in enumerate(chunks):
    print(f"  Processing chunk {i + 1}/{len(chunks)}: {chunk['id']}")

    # Generate embedding using litellm
    # Note: Using text-embedding-ada-002 as an example
    # You may want to use open-source alternatives like sentence-transformers
    try:
        response = embedding(model="text-embedding-ada-002", input=[chunk["text"]])
        embed = response["data"][0]["embedding"]
    except Exception as e:
        print(f"    Warning: Using mock embedding due to: {e}")
        # Fallback: Use ChromaDB's default embedding function
        embed = None  # ChromaDB will generate one

    # Add to collection
    collection.add(
        ids=[chunk["id"]],
        documents=[chunk["text"]],
        metadatas=[chunk["metadata"]],
        embeddings=[embed] if embed else None,
    )

print(f"\n✅ Indexed {len(chunks)} chunks in vector database")
print(f"   Collection: {collection.name}")
print(f"   Total items: {collection.count()}")

input("\n[Press Enter to continue to Step 3: Query...]")

# ============================================================================
# Step 3: Query the system
# ============================================================================

print("\n--- Step 3: Querying the RAG System ---\n")


def rag_query(question: str, top_k: int = 3) -> str:
    """
    Perform a RAG query: retrieve relevant chunks and generate answer.
    """
    print(f"Question: {question}\n")

    # Retrieve relevant chunks
    print(f"Searching for top-{top_k} relevant chunks...")
    results = collection.query(query_texts=[question], n_results=top_k)

    # Display retrieved chunks
    print(f"\nRetrieved {len(results['documents'][0])} chunks:")
    for i, (doc, metadata, distance) in enumerate(
        zip(results["documents"][0], results["metadatas"][0], results["distances"][0]),
        1,
    ):
        print(f"\n  Chunk {i}:")
        print(f"    Paper: {metadata['title']}")
        print(f"    Section: {metadata['section']}")
        print(f"    Similarity: {1 - distance:.3f}")
        print(f"    Text: {doc[:150]}...")

    # Build augmented context
    context_parts = [
        "You are a genomics research expert. Answer based on the provided paper excerpts. Cite sources.\n"
    ]
    context_parts.append("Retrieved Information:\n")

    for i, (doc, metadata) in enumerate(
        zip(results["documents"][0], results["metadatas"][0]), 1
    ):
        context_parts.append(
            f"\n[Source {i}] {metadata['title']} ({metadata['authors']}, {metadata['year']}) - {metadata['section'].title()}:"
        )
        context_parts.append(doc)

    context_parts.append(f"\n\nQuestion: {question}")
    context_parts.append(
        "\nAnswer based on the sources above. Include citations like [Source 1]."
    )

    full_context = "\n".join(context_parts)

    # Generate answer
    print("\nGenerating answer with LLM...")
    response = completion(
        model="anthropic/claude-sonnet-4-20250514",
        messages=[{"role": "user", "content": full_context}],
    )

    answer = response["choices"][0]["message"]["content"]
    return answer


# Example queries
queries = [
    "What sequencing methods were used in these studies?",
    "How many variants were identified per individual?",
    "What are the advantages of long-read sequencing?",
]

for query in queries:
    print("\n" + "=" * 80)
    answer = rag_query(query, top_k=3)
    print("\n" + "-" * 80)
    print("ANSWER:")
    print(answer)
    print("=" * 80)

    input("\n[Press Enter for next question...]")

# ============================================================================
# Step 4: Demonstrate metadata filtering
# ============================================================================

print("\n--- Step 4: Metadata Filtering ---\n")

print("Query with metadata filter: Only papers from 2023\n")

question = "What sequencing platforms were used?"
results = collection.query(
    query_texts=[question],
    n_results=5,
    where={"year": 2023},  # Filter by year
)

print(f"Retrieved {len(results['documents'][0])} chunks from 2023:")
for doc, metadata in zip(results["documents"][0], results["metadatas"][0]):
    print(f"\n  - {metadata['title']} ({metadata['year']})")
    print(f"    Section: {metadata['section']}")
    print(f"    Text: {doc[:100]}...")

print("\n" + "=" * 80)
print("Summary: RAG Pipeline Demonstrated")
print("=" * 80)
print("✅ Indexed 3 papers with 12 chunks")
print("✅ Generated embeddings for semantic search")
print("✅ Retrieved relevant chunks based on queries")
print("✅ Augmented context with retrieved information")
print("✅ Generated answers with source citations")
print("✅ Applied metadata filtering")
print("\n💡 Key advantage: Can scale to thousands of papers without")
print("   exceeding context window limits")
print("=" * 80)
