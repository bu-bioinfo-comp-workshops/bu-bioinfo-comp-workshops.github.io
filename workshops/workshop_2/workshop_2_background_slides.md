---
title: Workshop 2 Background Slides
layout: slides
footer: <a href="../workshop_2_instructions/index.html">Back to workshop 2</a>
---

# Workshop 2 Background Slides

---

## Ancient Genomes: New Challenges
- Ancient genome files can be hundreds of millions of base pairs
- File size and complexity require efficient code and high-performance computing

---

## Downloading Large Genomic Data
- Use tools like wget, curl, or programmatic Python to download large files
- Always verify file integrity (e.g., checksums)
- Consider storage and transfer limitations

---

## Efficient File Handling in Python
- Streaming and chunking allow you to process large files without loading them into memory
- Use generators, file handles, and libraries like BioPython

---

## Introduction to Compute Clusters
- Clusters provide distributed computing resources
- Typical workflow: write a job script, submit with qsub, monitor progress
- Learn basic cluster commands and job submission syntax

---

## Using LLMs for Scaling Up
- LLMs can help you adapt scripts for efficiency and cluster compatibility
- Effective prompts include file size, resource needs, and error handling
- Always review and test generated code before running on the cluster
