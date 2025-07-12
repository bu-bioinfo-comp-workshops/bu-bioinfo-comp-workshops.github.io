# Workshop 3 Introduction Slides

---

## Workflow Automation with Snakemake

- Make your genome analysis reproducible and shareable
- Refactor your previous scripts into a Snakemake workflow
- Use LLMs to help design, implement, and debug your workflow

---

## Problem Statement

- Refactor your scripts from previous workshops into a Snakemake workflow
- Automate steps for downloading data, running sequence analysis, and summarizing results
- Run your workflow on the compute cluster
- Summarize your workflow and findings for your PI

---

## Why Use Workflow Management?

- Ensures reproducibility and transparency
- Automates complex, multi-step analyses
- Facilitates collaboration and sharing

---

## What is Snakemake?

- A workflow management system for reproducible data analysis
- Uses a simple, readable syntax to define rules and dependencies
- Integrates easily with Python scripts and cluster computing

---

## Workshop Workflow: Problem → Prompt → Code → Debug → Result

- **Problem:** Define the workflow challenge
- **Prompt:** Craft an effective LLM prompt
- **Code:** Generate and run Snakemake rules
- **Debug:** Identify and fix errors (locally and on the cluster)
- **Result:** Summarize and interpret findings

---

## Getting Started: Example LLM Prompt

```
I need to refactor my genome analysis scripts into a Snakemake workflow that downloads an ancient genome FASTA file, computes sequence statistics, and summarizes the results. Please generate a Snakefile and example rule for running the analysis on a compute cluster.
```
