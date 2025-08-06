---
title: Workshop 2 Instructions
layout: single
toc: true
toc_sticky: true
---

# Workshop 2: Scaling Up and Using the Compute Cluster

## Introduction
In this workshop, you will build on your skills by working with a much larger bacterial genome dataset. We will pretend that the file is too large to process on your laptop, so you will learn how to use a compute cluster to perform your analysis. You will use LLMs to help adapt your scripts for large files and to run jobs on the cluster. This workshop is designed for students with little prior experience using high-performance computing resources.

## Template Repo
- [Workshop 2: Template Repo](https://github.com/bu-bioinfo-comp-workshops/workshop_2)
- [Github Classroom Link](https://classroom.github.com/a/ba_HL2g3)

## Supporting Materials
- [Workshop 2: Intro Slides](../workshop_2_introduction_slides/index.html)
- [Workshop 2: Background Slides](../workshop_2_background_slides/index.html)

## Problem Statement
You have received a large bacterial genome dataset (>100M base pairs) from your lab. Your PI wants you to calculate the same basic statistics as before (sequence length, GC content), but the file is too large to handle locally. Your job is to:
- Download a large bacterial genome FASTA file from a public resource (e.g. NCBI)
- Adapt your code to efficiently process large files
- Submit your analysis as a job to the compute cluster (using qsub or similar)
- Summarize your findings in a brief report

## Technical Skills Introduced
- Using VS Code and git for collaborative development
- Downloading large datasets from public genomics databases
- Python scripting for efficient file handling
- Basics of compute cluster usage (job submission with qsub)
- Prompt engineering and iterative debugging with LLMs

## Workshop Structure
1. **Setup:** Clone your workshop repository from GitHub Classroom, set up your environment, and review your previous scripts.
2. **Data Acquisition:** Use LLMs to help you write prompts for downloading a large genome FASTA file from a public database.
3. **Script Adaptation:** Prompt the LLM to help you modify your Python code to efficiently process large files (e.g., streaming, chunking).
4. **Cluster Job Submission:** Use LLMs to generate and debug cluster job scripts (e.g., qsub), submit your job, and monitor progress.
5. **Reporting:** Summarize your findings in a short markdown report. All files should be tracked in git and pushed to GitHub Classroom.

## Sample Initial Prompt
```
I need to process a large bacterial genome FASTA file (>100M bp)
that is too big for my laptop. Please generate Python code to
efficiently compute sequence length and GC content, and provide
an example qsub script to run this analysis on a compute cluster.
```

## Milestone 1

*Topics and Concepts*
- wget and FTP
- Qsub scripts
- Basic job monitoring

*Tasks*
- Download a bacterial genome of your choice from NCBI (https://www.ncbi.nlm.nih.gov/datasets/genome/)
using FTP and wrap it in a qsub script
- Submit your job to the compute cluster
- Monitor your job's progress

## Milestone 2

*Topics and Concepts*
- Using third party tools
- Python script and qsub script
- Conda environments - YML files

*Tasks*
- Adapt your download script to use NCBI Datasets CLI to download the bacterial genome
- Generate a python script to calculate the sequence length and GC content
- Generate a qsub script that submits your python code to generate the sequence length and GC content

## Milestone 3

*Topics and Concepts*
- Argparse
- Writing out files

*Tasks*
- Adapt your python code to use `argparse` to elegantly handle command-line arguments
- Adapt your python code to enable  writing out GC content and length to separately named files

## Milestone 4

*Topics and Concepts*
- Resource requests
- Advanced job tracking

*Tasks*
- Adapt your qsub script to request a different amount of resources



## Deliverables
By the end of this workshop, you will have created the following artifacts:

1. **Downloaded Large FASTA File**
   - A bacterial genome sequence file (FASTA format) obtained from a public database (e.g., NCBI).
   - Example: `bacterial_genome.fasta`

2. **Efficient Python Analysis Script**
   - A well-documented Python script that:
     - Reads the large FASTA file efficiently (e.g., streaming)
     - Computes sequence length and GC content
     - Prints or saves the results in a readable format
     - Has command-line arguments for input and output files
     - Allows you to name the outputs of GC content and length separately
   - Example: `analyze_bacterial_genome.py`

3. **Cluster Job Submission Script**
   - A script for submitting your Python analysis to the compute cluster (e.g., qsub script)
   - A modified script that requests a different amount of resources
   - Example: `run_analysis.qsub`

4. **Results Output**
   - A text or markdown file summarizing:
     - The sequence length 
     - The GC content (as a percentage)
     - Any additional notes or observations
   - Example: `bacterial_genome_results.md` or `bacterial_genome_results.txt`

5. **Brief Report**
   - A short markdown report (1–2 paragraphs) summarizing your approach, the results, and any challenges encountered. This should be clear enough to share with your PI or collaborators.
   - Example: `summary_report.md`

6. **Version-Controlled Repository**
   - All code files should be tracked in your git repository and pushed to GitHub Classroom as part of reproducible research best practices. This ensures your work is reproducible and easy to share with instructors and collaborators.
