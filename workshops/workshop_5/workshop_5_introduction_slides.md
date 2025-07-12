# Workshop 5 Introduction Slides

---

## Authenticating Ancient DNA and Quality Control

- Ancient DNA is often degraded and contaminated
- Authenticity and quality must be assessed before downstream analysis
- Use LLMs to help generate, debug, and interpret QC code

---

## Problem Statement

- Implement QC checks (read length distribution, GC content, damage patterns)
- Authenticate ancient DNA using computational methods
- Interpret QC outputs and summarize findings for your PI

---

## Why Quality Control for Ancient DNA?

- Ensures data is authentic and suitable for analysis
- Detects contamination, degradation, and other issues
- Guides decisions on whether to proceed or re-sequence

---

## Workshop Workflow: Problem → Prompt → Code → Debug → Result

- **Problem:** Define the QC and authentication challenge
- **Prompt:** Craft an effective LLM prompt
- **Code:** Generate and run QC scripts and rules
- **Debug:** Identify and fix QC issues
- **Result:** Summarize and interpret QC findings

---

## Getting Started: Example LLM Prompt

```
I need to perform quality control on ancient DNA FASTQ/FASTA files, including read length distribution, GC content, and damage pattern analysis. Please generate Python or bash scripts and Snakemake rules to automate these QC checks and summarize the results.
```
