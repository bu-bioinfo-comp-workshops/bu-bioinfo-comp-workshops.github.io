---
title: Workshop 4 Introduction Slides
layout: default
---

# Workshop 4 Introduction Slides

---

## Comparative Analysis of Multiple Ancient Samples

- Extend your workflow to analyze and compare multiple ancient mitochondrial genomes
- Automate batch downloads, run analyses, and generate comparative plots
- Use Snakemake and LLMs to streamline the process

---

## Problem Statement

- Download multiple ancient mitochondrial genome FASTA files from a public database
- Compute sequence statistics for each sample
- Generate comparative plots (e.g., GC content distribution)
- Summarize your approach and findings for your PI

---

## Why Compare Multiple Samples?

- Reveals biological variation and patterns across individuals
- Enables population-level insights
- Demonstrates the power of automation and reproducible workflows

---

## Workshop Workflow: Problem → Prompt → Code → Debug → Result

- **Problem:** Define the comparative analysis challenge
- **Prompt:** Craft an effective LLM prompt
- **Code:** Generate and run batch processing rules
- **Debug:** Identify and fix errors in batch workflows
- **Result:** Summarize and interpret comparative findings

---

## Getting Started: Example LLM Prompt

```
I need to download and analyze multiple ancient mitochondrial genome FASTA files from a public database. Please generate Snakemake rules and Python code to batch process each sample, compute sequence statistics, and generate a comparative GC content plot.
```
