---
title: Workshop Narrative
layout: default
---

I'm working on a series of computational workshops for bioinformatics PhD students. The workshops need to introduce key technical skills to the students if they don't have them already. Key skills are basic proficiency in: linux CLI, VS code,compute cluster usage, git and github, python, R, bash, and workflow management software (snakemake). We have a shared compute cluster (SCC) that we use for these workshops, and the materials are hosted on github and distributed to students using github classroom. VS code will be used as the development environment for all workshops.

I want to scaffold the workshops using a fictitious but realistic story about a genomics lab. The participant plays the role of a graduate student working in the lab, and is given a series of computational tasks to complete related to a project in the lab. The first tasks should be simple and only use a small subset of skills. Each subsequent task should build upon the previous one that is realistic to the overall narrative of the story. The story should be engaging and interesting to the students, and should provide a realistic context for the skills being taught.

LLM usage is central to these workshops. Each workshop follows the **Problem → Prompt → Code → Debug → Result** cycle:

1. **Problem Statement**: Clear biological/bioinformatics challenge with specific output goal
2. **Prompt Engineering**: Students craft effective LLM prompts to generate initial code. 
3. **Code Generation**: Use LLM to create starting solution
4. **Run & Debug**: Execute code, identify errors, return to LLM for fixes
5. **Iterate**: Repeat LLM interaction until achieving target result
6. **Add New Features**: The problem statement is augmented to include new features.
7. **Revise/Append**: The problem statement is revised to include new features.
8. **Repeat**: Repeat steps 2-7 until the workshop is complete.

The key meta skill I want students to leave the workshops with is the ability to use LLMs to help understand a problem statement, translate it into technical requirements, generate initial code, debug it, and iterate until a solution is reached. Students also need to understand the limitations of LLMs, what they're good for, and what they're not good for.

Here are the high level tasks I'm thinking for the workshops:

1. Download a small genome (< 1M base pairs) from NCBI and calculate basic statistics.
    - Skills: VS code, git, github, basic python
2. Download a large genome (>100M base pairs) from NCBI and calculate basic statistics
    - Skills: VS code, git, github, basic python, compute cluster usage (qsub)
3. Refactor the scripts from above into a snakemake workflow
    - Skills: VS code, git, github, basic python, compute cluster usage (qsub), basic snakemake
4. Download many small genomes from NCBI, calculate basic statistics, and compare them
    - Skills: VS code, git, github, basic python, compute cluster usage (qsub), basic snakemake for downloading many genomes

There are many different possible story settings.