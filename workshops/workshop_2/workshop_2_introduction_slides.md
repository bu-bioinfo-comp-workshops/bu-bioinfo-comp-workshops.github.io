# Workshop 2 Introduction Slides

---

## Scaling Up: Ancient Genome Analysis on the Cluster

- You now have a much larger dataset: a full ancient genome (>100M bp)
- The file is too big for your laptop! Time to use the compute cluster.
- You'll learn to adapt your scripts and submit jobs to the cluster with LLM assistance.

---

## Problem Statement

- Download a large ancient genome FASTA file from a public database.
- Adapt your code to efficiently process large files.
- Submit your analysis as a job to the compute cluster (qsub).
- Summarize your findings for your PI.

---

## Why Use a Compute Cluster?

- Large files require more memory and processing power than a laptop can provide
- Clusters allow parallel, high-throughput analysis
- Learning to use clusters is essential for modern genomics research

---

## Workshop Workflow: Problem → Prompt → Code → Debug → Result

- **Problem:** Define the computational challenge
- **Prompt:** Craft an effective LLM prompt
- **Code:** Generate and run scalable code
- **Debug:** Identify and fix errors (locally and on the cluster)
- **Result:** Summarize and interpret findings

---

## Getting Started: Example LLM Prompt

```
I need to process a large ancient genome FASTA file (>100M bp) that is too big for my laptop. Please generate Python code to efficiently compute sequence length and GC content, and provide an example qsub script to run this analysis on a compute cluster.
```
