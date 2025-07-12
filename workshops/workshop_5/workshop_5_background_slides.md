# Workshop 5 Background Slides

---

## Ancient DNA Quality Challenges
- Ancient DNA is highly fragmented and chemically modified
- Common issues: short reads, high error rates, contamination

---

## QC Metrics and Tools
- Read length distribution: identifies fragmentation
- GC content: checks for expected nucleotide composition
- Damage patterns: reveals ancient DNA authenticity (e.g., C→T transitions)
- Tools: Python scripts, bash, specialized packages (e.g., mapDamage)

---

## Integrating QC into Workflows
- Automate QC steps with Snakemake
- Modular rules for each metric
- Output tables and plots for interpretation

---

## Using LLMs for QC and Interpretation
- LLMs can help write and debug QC scripts
- Effective prompts describe the QC metric and expected outputs
- Always review and interpret results critically
