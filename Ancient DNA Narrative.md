# Ancient DNA Analysis Team: Narrative and Workshop Sequence

## Narrative Overview
You are a new graduate student in the Ancient Genomics Lab. Your lab specializes in extracting and sequencing DNA from archaeological bone samples. The current project is to analyze DNA from bones discovered at a recently excavated site, with the goal of comparing these ancient genomes to modern populations and uncovering clues about ancient human migrations.

Your PI has tasked you with a series of computational challenges, each representing a real step in an ancient DNA project. As you progress, you’ll learn to use LLMs to translate research questions into computational workflows, debug code, and iterate on your solutions.

---

## Workshop Sequence Sketch

### Workshop 1: Download and Explore Ancient DNA Data
- **Narrative Context:** You’ve received raw sequencing data from the field team. Your first task is to download a small ancient mitochondrial genome dataset from a public database and calculate basic statistics.
- **Skills:** VS Code, git, github, basic python
- **LLM Tasks:** Prompt LLM to generate code for downloading and parsing FASTA files, calculating sequence length, GC content, and simple summary statistics.
- **Meta-Skill Focus:** Translating a biological question into a data task, prompt engineering, iterating on LLM-generated code.

---

### Workshop 2: Scaling Up and Using the Compute Cluster
- **Narrative Context:** The lab has sequenced a full ancient genome (>100M bp). You need to download this large dataset and run the same statistics, but now the file is too big for your laptop.
- **Skills:** VS Code, git, github, python, compute cluster usage (qsub)
- **LLM Tasks:** Prompt LLM to adapt scripts for large files and to run on the cluster.
- **Meta-Skill Focus:** Modifying prompts for scale, understanding compute resource limitations, debugging cluster jobs.

---

### Workshop 3: Workflow Automation with Snakemake
- **Narrative Context:** Your PI wants your analysis to be reproducible. You must refactor your scripts into a Snakemake workflow so other lab members can use them.
- **Skills:** VS Code, git, github, python, compute cluster, Snakemake basics
- **LLM Tasks:** Prompt LLM to help design and implement a Snakemake workflow for data download and statistics.
- **Meta-Skill Focus:** Breaking down analysis into modular steps, using LLMs for workflow design, debugging workflow errors.

---

### Workshop 4: Comparative Analysis of Multiple Ancient Samples
- **Narrative Context:** The excavation yielded several bone samples from different individuals. Download multiple ancient mitochondrial genomes, calculate statistics for each, and compare them to modern samples.
- **Skills:** VS Code, git, github, python, compute cluster, Snakemake
- **LLM Tasks:** Prompt LLM to automate batch downloads, loop over samples, and generate comparative plots.
- **Meta-Skill Focus:** Prompting for automation, handling multiple datasets, interpreting and visualizing results.

---

### Workshop 5: Authenticating Ancient DNA and Quality Control
- **Narrative Context:** Ancient DNA is often degraded and contaminated. Implement quality control checks (e.g., read length distribution, damage patterns) using LLM-assisted code generation.
- **Skills:** Python, bash, cluster, Snakemake, basic QC tools
- **LLM Tasks:** Prompt LLM to generate code for QC metrics, interpret QC outputs, and iterate based on findings.
- **Meta-Skill Focus:** Prompting for domain-specific tasks, integrating new tools, critical evaluation of LLM output.

---

### Workshop 6: Reproducibility and Collaboration
- **Narrative Context:** Prepare your workflow and results for publication and sharing with collaborators. Use git, GitHub, and markdown to document your analysis.
- **Skills:** git, GitHub, markdown, workflow documentation
- **LLM Tasks:** Prompt LLM to help write clear documentation, README files, and collaborative instructions.
- **Meta-Skill Focus:** Prompting for documentation, communicating computational results, reflecting on the LLM-assisted process.

---

## How This Narrative Supports Learning Goals
- **Engagement:** Students are immersed in a realistic research scenario with tangible biological questions.
- **Skill Progression:** Each workshop builds on the last, scaffolding both technical and meta-skills.
- **LLM Integration:** Students repeatedly use LLMs for code generation, debugging, and workflow design, reinforcing prompt engineering and iterative problem-solving.
