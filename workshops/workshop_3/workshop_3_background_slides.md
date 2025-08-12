---
title: Workshop 3 Background Slides
layout: slides
footer: <a href="../workshop_3_instructions/index.html">Back to workshop 3</a>
---

# Workshop 3 Background Slides

---

## Workflow Management in Bioinformatics
- Complex analyses require multiple steps and tools
- Manual execution is error-prone and hard to reproduce
- Workflow managers (like Snakemake) automate and document the process

---

## Introduction to Snakemake
- Snakemake uses rules to define how files are created from input data
- Rules specify input, output, scripts, and resources
- Workflows are defined in a `Snakefile` (Python-like syntax)

---

## The `Snakefile`

- A `Snakefile` defines rules for creating files
- At minimum, a rule has:
    - a name
    - `output`: the files the rule creates
    - `shell`: the shell command that creates the files
- When creating a file from another file, the rule also has:
    - `input`: the files the rule depends on

---

## Example Rule

Assume we wrote the script `summarize_genome.py` that accepts a FASTA file as input and creates a summary file as output.

```python
rule summarize_genome:
    input:
        "data/genome.fasta"
    output:
        "results/genome_summary.txt"
    shell:
        "python scripts/summarize_genome.py {input} {output}"
```

---

## Example Rule cont'd

```python
rule summarize_genome:
    input:
        "data/genome.fasta"
    output:
        "results/genome_summary.txt"
    shell:
        "python scripts/summarize_genome.py {input} {output}"
```

The `input` and `output` values are inserted into the command and executed:

```bash
python scripts/summarize_genome.py data/genome.fasta \
    results/genome_summary.txt
```

---

## The `all` rule

- Snakefiles have a special rule called `all` that defines the files that 
should be created by the workflow
- The `all` rule should come first, and only have `input` specified

```python
rule all:
    input:
        "results/genome_summary.txt"

rule summarize_genome:
    # rule definition from previous
```

---

<section data-background-image="/assets/images/snakemake_rule.excalidraw.svg" data-background-size="contain">
</section>

---

## Example Rule cont'd

```
$ ls
data scripts Snakefile
$ snakemake -j 1
```

---

## Running Snakemake on a Compute Cluster
- Snakemake can submit jobs to clusters using qsub or other schedulers
- Cluster profiles and job scripts help manage resources
- Monitor job status and troubleshoot errors

---

## Using LLMs for Workflow Design
- LLMs can help draft rules, debug errors, and suggest improvements
- Effective prompts describe the workflow steps and expected outputs
- Always review and test generated workflows for correctness
