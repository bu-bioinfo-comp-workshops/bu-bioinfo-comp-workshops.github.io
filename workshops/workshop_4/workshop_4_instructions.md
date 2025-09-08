---
title: Workshop 4 - Comparative Analysis of Multiple Samples
layout: single
toc: true
toc_sticky: true
---

# Introduction
In this workshop, you will extend your workflow to handle and compare multiple microbe genomes. You will use Snakemake and LLMs to automate batch downloads, run analyses on many samples, and generate comparative plots. This workshop is designed for students with little prior experience handling multiple datasets or comparative genomics.

# Template Repo
- [Workshop 4](https://github.com/bu-bioinfo-comp-workshops/workshop_4)

# Supporting Materials
- [Workshop 4: Intro Slides](../workshop_4_introduction_slides/index.html)
- [Workshop 4: Background Slides](../workshop_4_background_slides/index.html)

# Problem Statement
A collection of microbe genome samples has been obtained from different environments. Your PI wants to know how these microbe genomes compare to each other and to reference genomes. Your job is to:
- Download multiple microbe genome FASTA files from a public resource (e.g., NCBI)
- Automate the analysis to compute statistics (sequence length, GC content) for each sample
- Generate comparative plots (e.g., GC content distribution)
- Summarize your approach and findings in a brief report

# Technical Skills Introduced
- Using Snakemake for batch processing and automation
- Downloading and managing multiple datasets
- Python scripting for looping over files and comparative analysis
- Generating plots with Python (matplotlib or similar)
- Prompt engineering and iterative debugging with LLMs

# Workshop Structure
1. **Setup:** Clone your workshop repository from GitHub Classroom, set up your environment, and review your previous workflow.
2. **Batch Data Acquisition:** Use LLMs and Snakemake to automate downloading multiple FASTA files from a public database.
3. **Automated Analysis:** Prompt the LLM to help you adapt your workflow to process each sample and collect statistics.
4. **Comparative Visualization:** Use LLMs and Python to generate comparative plots of GC content and sequence length across samples.
5. **Reporting:** Summarize your approach and findings in a short markdown report. All files should be tracked in git and pushed to GitHub Classroom.

# Sample Initial Prompt
```
I need to download and analyze multiple microbe genome FASTA files from a public database. Please generate Snakemake rules and Python code to batch process each sample, compute sequence statistics, and generate a comparative GC content plot.
```
# Clone the github classroom repository
Clone the github classroom repository and open your VSCode session within the
repo. 

Try and accomplish the following milestones working directly in the repo
you create.

# Milestones

## Milestone 1

*Topics and Concepts*
- Generalized Snakemake rules using wildcards
- Batch downloading with Snakemake
- Using a CSV to store sample information

*Tasks*
- Browse NCBI datasets to identify at least three microbe genomes from a public database. Locate the accession numbers of the genomes you wish to download.
- Store the accession numbers in a CSV file or as a python list at the top of your Snakefile.
- Write a Snakemake rule that uses wildcards to generalize the genome download by constructing output fasta file names from the accession number.
- Use the NCBI Datasets CLI to download the genomes as fasta files using the accession numbers you identified before.

## Milestone 2

*Topics and Concepts*
- Executing Snakemake workflow with multiple samples

*Tasks*
- Execute the Snakemake workflow with multiple samples
- Submit jobs on the compute cluster

## Milestone 4

*Topics and Concepts*
- Genome statistics, including GC content 
- Organizing results into a single file

*Tasks*
- Organize the results of the individual genome analysis jobs into a single CSV file, where rows are genomes and columns are statistics

## Milestone 5

*Topics and Concepts*
- k-mer based GC Content Distributions

*Tasks*
- Write a python script or snakemake rule that decomposes a given genome sequence into $k$-mers and computes the GC content of each $k$-mer
- As an LLM for guidance on how to implement this analysis

## Milestone 6

*Topics and Concepts*
- Comparative genome statistics

*Tasks*
- Generate comparative genome statistics for the genomes you downloaded. We will compare the overall GC content you calculated, as well as the k-mer based GC content distributions.
- Generate a simple table of overall GC content for each genome.
- Generate histograms of the k-mer based GC content distributions. You may consider adding the overall GC content as a notation on the plot. You might also consider adding all GC content distributions on a single plot for the purposes of comparison.

# Deliverables
By the end of this workshop, you will have created the following artifacts:

1. **Batch-Processing Snakemake Workflow**
   - A Snakefile and any config or rule files for batch downloading and analysis of multiple samples
   - Example: `Snakefile`, `config.yaml`, `rules/`

2. **Automated Analysis Scripts**
   - Python scripts for computing overall GC content and k-mer based GC content distributions
  - Example: `scripts/compute_gc_content.py`
  - Example: `scripts/compute_kmer_gc_content_distribution.py`

3. **Comparative Tables and Plots**
   - Tables comparing GC content across samples
   - Example: `results/gc_content_comparison.png`, `results/sequence_length_comparison.png`

4. **Workflow Output Results**
   - Output files summarizing statistics for each sample
   - Example: `results/sample_stats.tsv`, `results/comparative_summary.md`

5. **Brief Report**
   - A short markdown report (1–2 paragraphs) summarizing your workflow design, comparative findings, and any challenges encountered. This should be clear enough to share with your PI or collaborators.
   - Example: `comparative_report.md`

6. **Version-Controlled Repository**
   - All code and workflow files should be tracked in your git repository and pushed to GitHub Classroom as part of reproducible research best practices. This ensures your work is reproducible and easy to share with instructors and collaborators.
