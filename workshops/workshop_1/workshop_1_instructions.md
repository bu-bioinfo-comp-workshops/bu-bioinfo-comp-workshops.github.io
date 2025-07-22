---
layout: single
title: Workshop 1 - Download and Explore Ancient DNA Data
toc: true
toc_sticky: true
---

# Introduction
Welcome to your first hands-on computational workshop as a new graduate student in an ancient genomics lab! This session is designed for students with little prior computational experience. You will use GitHub Classroom to access your workshop repository and learn essential skills by working with real ancient DNA data. Your main goal is to download a small ancient mitochondrial genome dataset from a public database and calculate basic statistics. Throughout, you will use Large Language Models (LLMs) to help translate biological questions into code, debug your scripts, and iterate until you reach a solution. This workshop follows the Problem → Prompt → Code → Debug → Result cycle.

# Supporting Materials
- [Workshop 1: Intro Slides](/workshops/workshop_1/workshop_1_introduction_slides/index.html)
- [Workshop 1: Background Slides](/workshops/workshop_1/workshop_1_background_slides/index.html)

# Problem Statement
You have received raw sequencing data from the field team. Your PI wants to know: "What are the basic characteristics of this ancient mitochondrial genome?" Your job is to:
- Download a small ancient mitochondrial genome dataset from a public resource (e.g., Allen Ancient DNA Resource, NCBI)
- Calculate basic statistics (sequence length, GC content)
- Summarize your findings in a brief report

# Technical Skills Introduced
- Using VS Code for code development
- Basic git and GitHub for version control
- Downloading data from public genomics databases
- Python scripting for sequence analysis
- Prompt engineering and iterative debugging with LLMs

# Workshop Workflow

![Workshop Workflow](/assets/images/workshop_flow.excalidraw.svg)

## Workshop Structure
1. **Setup** (with GitHub Classroom):
   - Clone your workshop repository from GitHub Classroom.
   - Set up your coding environment (VS Code) and explore the project structure.
2. **Data Acquisition:**
   - Use LLMs to help you write prompts for downloading a mitochondrial genome FASTA file from a public database (e.g., AADR or NCBI).
3. **Sequence Exploration:**
   - Prompt the LLM to generate Python code for parsing the FASTA file and calculating sequence length and GC content.
4. **Debug & Iterate:**
   - Run your code, use LLMs to help debug errors, and refine your prompts and scripts until you get correct results.
5. **Reporting:**
   - Summarize your findings in a short markdown report. All files should be tracked in git and pushed to GitHub.

At certain points, we will discuss several different ways of accomplishing the stated goals and the situations in when you would choose
to use a specific approach vs. others. We will ask you to refine your approach using some of the best practices we discuss and introduce
to you. 


## Sample Initial Prompt

> I need to download a small ancient mitochondrial genome FASTA file from a public database (such as the Allen Ancient DNA Resource or NCBI). Please help me brainstorm ways I can accomplish this.

## Guidelines
   - Please work entirely on the SCC
   - Develop your own methods you are comfortable with to accomplish the goals

## Schedule

**1st hour**

Interactive Demo of SCC OnDemand and basic git / github setup (50 minutes)
- Setup SSH keys (https://www.bu.edu/tech/support/research/system-usage/connect-scc/access-and-security/using-scc-with-github-2fa/#AUTH)
- Understand VsCode core features and install common plugins
- Basic SCC Structure (head node, compute nodes, interactive jobs)
- Home directory and project directory structures

Break (10 minutes)

**2nd hour**
Objective 1 (20 minutes)
- Develop a method or series of steps that downloads a single genome and calculates the GC content

Discussion of approach (10 minutes)
- Demonstration of an approach for accomplishing the stated goals
- Discussion of the strengths and weaknesses of the approach and possible points of improvement

Modifications to your approach and discussion (30 mins)

**3rd hour**

New modifications to your approach (30 minutes)

Discussion of approach (30 minutes)
- Demonstration of an approach for accomplishing the stated goals
- Discussion of the strengths and weaknesses of the approach and possible points of improvement


## Deliverables
By the end of this workshop, you will have created the following artifacts:

1. **Downloaded FASTA File**
   - A small ancient mitochondrial genome sequence file (FASTA format) obtained from a public database (e.g., AADR or NCBI).
   - Example: `ancient_mtDNA.fasta`

2. **Python Analysis Script**
   - A well-documented Python script that:
     - Reads the downloaded FASTA file
     - Computes sequence length and GC content
     - Prints or saves the results in a readable format
   - Example: `analyze_mtDNA.py`

3. **Results Output**
   - A text or markdown file summarizing:
     - The sequence length
     - The GC content (as a percentage)
     - Any additional notes or observations
   - Example: `results.md` or `results.txt`

4. **(Optional) Visualization**
   - A simple plot (e.g., pie chart or bar plot) of base composition or GC content, generated using Python (matplotlib or similar)
   - Example: `gc_content_plot.png`

5. **Brief Report**
   - A short markdown report (1–2 paragraphs) summarizing your approach, the results, and any challenges encountered. This should be clear enough to share with your PI or collaborators.
   - Example: `summary_report.md`

6. **Version-Controlled Repository**
   - All code files should be tracked in your git repository and pushed to GitHub Classroom as part of reproducible research best practices. This ensures your work is reproducible and easy to share with instructors and collaborators.
