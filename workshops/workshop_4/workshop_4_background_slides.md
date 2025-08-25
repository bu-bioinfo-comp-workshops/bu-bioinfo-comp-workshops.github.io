---
title: Workshop 4 Background Slides
layout: slides
footer: <a href="../workshop_4_instructions/index.html">Back to workshop 4</a>
---

# Workshop 4 Background Slides

---

## Comparative Genomics: Key Concepts
- Comparing genomes reveals similarities and differences across individuals or populations
- Batch analysis enables efficient, large-scale comparisons

---

## Batch Processing with Snakemake
- Snakemake can automate repetitive tasks across many samples
- Use wildcards and config files to generalize rules
- Modular workflows improve reproducibility and scalability

---

## Generalizing Rules with Wildcards
- *Wildcards* define patterns in file names
- Defined with curly braces: `"{sample}.txt"`
- Strings with wildcards are provided to `input` and `output` cluases in rule definitions

---

## Wildcard example

```python
rule calculate_gc:
    input:
        "data/{sample}.fasta"
    output:
        "results/{sample}_gc.txt"
    shell:
        "python scripts/gc_content.py {input} > {output}"
```

`{sample}` is a wildcard that is defined in the rule definition.

---

```python
rule all:
    input:
        "results/sampleA_gc.txt"

rule calculate_gc:
    input:
        "data/{sample}.fasta"
    output:
        "results/{sample}_gc.txt"
    shell:
        "python scripts/gc_content.py {input} > {output}"
```

Snakemake will run:

```
python scripts/gc_content.py data/sampleA_gc.txt > \
    results/sampleA_gc.txt
```

---


<section data-background-image="/assets/images/snakemake_rule_wildcard.excalidraw.svg" data-background-size="contain">
</section>

---

```python
rule all:
    input:
        "results/sampleA_gc.txt",
        "results/sampleB_gc.txt",
        "results/sampleC_gc.txt"

rule calculate_gc:
    input:
        "data/{sample}.fasta"
    output:
        "results/{sample}_gc.txt"
    shell:
        "python scripts/gc_content.py {input} > {output}"
```

Snakemake will run the rule three times, once for each sample in the `input` of rule `all`.

---

## The `expand()` function

- Snakemake defines a function called `expand()` that can be used to generate a list of files based on a pattern
- It accepts two arguments:
    - A string with one or more wildcard patterns
    - Named arguments for each wildcard that accept lists of values

---

## `expand()` example

```python
samples = ["sampleA", "sampleB", "sampleC"]
expand("results/{sample}_gc.txt", sample=samples)
```

produces a list of strings:

```python
["results/sampleA_gc.txt",
 "results/sampleB_gc.txt",
 "results/sampleC_gc.txt"]
```
---

## Complete example

```python

samples = ["sampleA", "sampleB", "sampleC"]
rule all:
    input:
        expand("results/{sample}_gc.txt", sample=samples)

rule calculate_gc:
    input:
        "data/{sample}.fasta"
    output:
        "results/{sample}_gc.txt"
    shell:
        "python scripts/gc_content.py {input} > {output}"
```

---

## Running multiple jobs

```
$ ls
data scripts Snakefile
$ snakemake -j 3 # ← run all three jobs concurrently
```
 
---

# Genome Statistics

---

## Basic Genomic Characteristics

- GC content
- Sequence length
- k-mer frequency

---

## Genome Complexity

---

## Generating Comparative Plots
- Visualizations (bar plots, boxplots) make patterns and differences clear
- Plots can summarize GC content, sequence length, and more

---

## Using LLMs for Batch Analysis
- LLMs can help write loops, batch rules, and plotting code
- Effective prompts describe the batch task and desired outputs
- Always review and test generated code for correctness
