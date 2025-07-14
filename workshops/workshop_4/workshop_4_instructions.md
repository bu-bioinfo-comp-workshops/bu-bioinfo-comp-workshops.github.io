---
title: Workshop 4 Instructions
layout: default
---

# Workshop 4: Comparative Analysis of Multiple Ancient Samples

## Introduction
In this workshop, you will extend your workflow to handle and compare multiple ancient mitochondrial genome samples. You will use Snakemake and LLMs to automate batch downloads, run analyses on many samples, and generate comparative plots. This workshop is designed for students with little prior experience handling multiple datasets or comparative genomics.

## Supporting Materials
- [Workshop 4: Intro Slides](workshop_4_introduction_slides.html)
- [Workshop 4: Background Slides](workshop_4_background_slides.html)

## Problem Statement
The excavation has yielded several bone samples from different individuals. Your PI wants to know how these ancient mitochondrial genomes compare to each other and to modern samples. Your job is to:
- Download multiple ancient mitochondrial genome FASTA files from a public resource (e.g., AADR or NCBI)
- Automate the analysis to compute statistics (sequence length, GC content) for each sample
- Generate comparative plots (e.g., GC content distribution)
- Summarize your approach and findings in a brief report

## Technical Skills Introduced
- Using Snakemake for batch processing and automation
- Downloading and managing multiple datasets
- Python scripting for looping over files and comparative analysis
- Generating plots with Python (matplotlib or similar)
- Prompt engineering and iterative debugging with LLMs

## Workshop Structure
1. **Setup:** Clone your workshop repository from GitHub Classroom, set up your environment, and review your previous workflow.
2. **Batch Data Acquisition:** Use LLMs and Snakemake to automate downloading multiple FASTA files from a public database.
3. **Automated Analysis:** Prompt the LLM to help you adapt your workflow to process each sample and collect statistics.
4. **Comparative Visualization:** Use LLMs and Python to generate comparative plots of GC content and sequence length across samples.
5. **Reporting:** Summarize your approach and findings in a short markdown report. All files should be tracked in git and pushed to GitHub Classroom.

## Sample Initial Prompt
```
I need to download and analyze multiple ancient mitochondrial genome FASTA files from a public database. Please generate Snakemake rules and Python code to batch process each sample, compute sequence statistics, and generate a comparative GC content plot.
```

## Deliverables
By the end of this workshop, you will have created the following artifacts:

1. **Batch-Processing Snakemake Workflow**
   - A Snakefile and any config or rule files for batch downloading and analysis of multiple samples
   - Example: `Snakefile`, `config.yaml`, `rules/`

2. **Automated Analysis Scripts**
   - Python scripts for looping over multiple FASTA files and computing statistics
   - Example: `scripts/analyze_multiple.py`

3. **Comparative Plots**
   - Plots comparing GC content and sequence length across samples (e.g., bar plots, boxplots)
   - Example: `results/gc_content_comparison.png`, `results/sequence_length_comparison.png`

4. **Workflow Output Results**
   - Output files summarizing statistics for each sample
   - Example: `results/sample_stats.tsv`, `results/comparative_summary.md`

5. **Brief Report**
   - A short markdown report (1–2 paragraphs) summarizing your workflow design, comparative findings, and any challenges encountered. This should be clear enough to share with your PI or collaborators.
   - Example: `comparative_report.md`

6. **Version-Controlled Repository**
   - All code and workflow files should be tracked in your git repository and pushed to GitHub Classroom as part of reproducible research best practices. This ensures your work is reproducible and easy to share with instructors and collaborators.
