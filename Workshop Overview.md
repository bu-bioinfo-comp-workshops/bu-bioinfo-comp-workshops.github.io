---
title: Workshop Overview
layout: default
---

# Workshop Overview

The goal of these workshops is to give participants hands on experience with computational tools and skills required by modern bioinformatics and computational biology research. The workshops are designed to be interactive and engaging, with a focus on practical application of the skills covered.

The workshops are organized as a series of realistic use cases that participants will work through in a hands on manner. The workshops are designed to be self contained, with each workshop building on the skills learned in the previous workshop.

# Covered Skills

- Large language models
    - basic prompt engineering and refinement
    - code generation
    - debugging
- Linux
    - command line interface
    - basic navigation and file manipulation
    - basic bash scripting
    - conda 
- version control
    - git
    - github
- shared compute cluster (SCC)
    - SCC ondemand
    - GNU modules usage
    - basic computional resource management (understanding CPU, RAM, GPU)
    - memory resource usage
    - job submission and monitoring
- computational environments and tools
    - VS code
    - GNU modules
    - conda
    - Docker/singularity
    - computational notebooks
- workflow management software
    - snakemake
- basic programming
    - python
    - R
    - bash

# Workshop Descriptions

## Workshop 1 - Basic Skills

### Problem Statement

Original: Your quality report from Workshop 1 identified adapter contamination and low-quality read ends. You need to clean the data using HPC resources and verify the improvement quantitatively.

Updated: Develop a small workflow that downloads public sequencing data from the SRA and performs basic quality control. 

Original: You have received FASTQ files from a bacterial genome sequencing project. Your collaborator wants to know: "Are these sequences good quality? Should we proceed with assembly or re-sequence?" You need to provide a definitive answer with supporting data.

Updated: You want to develop a small workflow to download the human reference genome from gencode and provide some basic summary statistics. 

### Skills

- Basic Linux commands
- Basic command line navigation
    - Posix conventions and argument parsing
- Basic Shared Compute Cluster (SCC) Usage
- GNU modules usage
- Basic git usage