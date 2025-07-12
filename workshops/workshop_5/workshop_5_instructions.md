# Workshop 5: Authenticating Ancient DNA and Quality Control

## Introduction
In this workshop, you will learn how to authenticate ancient DNA data and perform essential quality control (QC) checks. Ancient DNA is often degraded and contaminated, so verifying its authenticity and quality is a crucial step in any analysis. You will use LLMs to help generate and debug QC code, interpret outputs, and iterate on your workflow. This workshop is designed for students with little prior experience in QC or ancient DNA authentication.

## Problem Statement
Your PI wants to ensure that the ancient DNA data you are analyzing is authentic and of sufficient quality for downstream analysis. Your job is to:
- Implement quality control checks (e.g., read length distribution, GC content, damage patterns)
- Authenticate ancient DNA using computational methods
- Interpret QC outputs and summarize findings in a brief report

## Technical Skills Introduced
- Python and bash scripting for QC analysis
- Using Snakemake to automate QC steps
- Interpreting QC metrics (read length, GC content, damage patterns)
- Integrating QC tools and scripts into workflows
- Prompt engineering and iterative debugging with LLMs

## Workshop Structure
1. **Setup:** Clone your workshop repository from GitHub Classroom, set up your environment, and review your previous workflows.
2. **QC Tool Selection:** Use LLMs to help you identify and select appropriate QC tools or write custom scripts (e.g., for read length, GC content, damage patterns).
3. **QC Implementation:** Prompt the LLM to help you write and integrate QC scripts into your Snakemake workflow.
4. **Interpretation:** Use LLMs to help interpret QC outputs and decide if the data is authentic and usable.
5. **Reporting:** Summarize your QC approach, findings, and recommendations in a short markdown report. All files should be tracked in git and pushed to GitHub Classroom.

## Sample Initial Prompt
```
I need to perform quality control on ancient DNA FASTQ/FASTA files, including read length distribution, GC content, and damage pattern analysis. Please generate Python or bash scripts and Snakemake rules to automate these QC checks and summarize the results.
```

## Deliverables
By the end of this workshop, you will have created the following artifacts:

1. **QC Scripts and Tools**
   - Python or bash scripts for QC analysis (read length, GC content, damage patterns)
   - Example: `scripts/qc_read_length.py`, `scripts/qc_damage.sh`

2. **Snakemake Workflow Integration**
   - Updated Snakefile and rule files to automate QC steps
   - Example: `Snakefile`, `rules/qc.smk`

3. **QC Output Files**
   - Output files summarizing QC metrics for each sample (e.g., tables, plots)
   - Example: `results/read_length_distribution.png`, `results/gc_content_qc.txt`, `results/damage_patterns.tsv`

4. **Interpretation and Recommendation Report**
   - A short markdown report (1–2 paragraphs) summarizing QC findings, authenticity assessment, and recommendations for downstream analysis
   - Example: `qc_report.md`

5. **Version-Controlled Repository**
   - All code and workflow files should be tracked in your git repository and pushed to GitHub Classroom as part of reproducible research best practices. This ensures your work is reproducible and easy to share with instructors and collaborators.
