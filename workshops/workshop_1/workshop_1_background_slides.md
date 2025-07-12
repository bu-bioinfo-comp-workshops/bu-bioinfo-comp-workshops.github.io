# Workshop 1 Background Slides

---

## Ancient DNA: Key Concepts
- Ancient DNA (aDNA) is often fragmented and chemically damaged
- Mitochondrial genomes are commonly used due to their abundance and small size
- Public resources: Allen Ancient DNA Resource (AADR), NCBI GenBank

---

## Downloading Genomic Data
- Most public databases provide FASTA files for genome sequences
- Data can be downloaded via web browser, curl, wget, or programmatically (e.g., Python requests)
- Always check data licensing and usage restrictions

---

## FASTA File Format
- Text-based format for nucleotide or protein sequences
- Begins with a ">" header line, followed by sequence lines
- Example:
```
>Sample1 mtDNA
ATGCGT...
```

---

## Calculating Sequence Statistics
- **Sequence length**: Number of nucleotides
- **GC content**: Percentage of G and C bases
- Useful for quality checks and basic characterization
- Can be computed with simple Python scripts

---

## Using LLMs for Bioinformatics
- LLMs can help write, debug, and improve code
- Effective prompts are clear, specific, and goal-oriented
- Always verify outputs and iterate as needed
