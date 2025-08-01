# Prompt for Creating Student-Facing Workshop Materials

**Objective:**  
Create a student materials directory for this workshop that mirrors the structure and pedagogical approach of the student-facing materials in `workshop_1/workshop_1`. These materials are intended for hands-on use by students during the workshop and should provide scaffolded code, step-by-step instructions, and supporting documentation. The materials should be suitable for distribution via GitHub Classroom.

---

## 1. Directory and File Structure

Create a new directory under the workshop (e.g., `workshop_N/workshop_N/`) with the following structure:

- `INSTRUCTIONS.md` — Step-by-step, scaffolded instructions for students to follow throughout the workshop.
- `README.md` — Overview of the workshop, learning goals, and usage instructions for the student repo.
- `requirements.txt` — List of Python dependencies needed for the workshop.
- `src/` — Directory for code scripts, each scaffolded for the workshop tasks (e.g., data download, analysis, visualization).
- `data/`
  - `README.md` — Instructions/notes on expected input data.
- `results/`
  - `README.md` — Instructions/notes on expected output/results.
- `templates/`
  - `results_template.md` — Template for results summary.
  - `summary_report_template.md` — Template for the final report.
- `docs/`
  - `sample_prompts.md` — Example LLM prompts relevant to this workshop.
  - `troubleshooting.md` — Common issues and solutions related to the workshop’s technical focus.

Include any additional files or directories as needed for the specific workshop.

---

## 2. Intent and Approach

- **Scaffold, Don’t Solve:**  
  All code files in `src/` should be scaffolded, not fully solved. Include function headers, docstrings, and comments indicating where students should add their code. Use `TODO` comments to signal tasks for students.
- **Stepwise Guidance:**  
  The `INSTRUCTIONS.md` file should walk students through the workshop in a logical, incremental fashion. Each step should reference specific scripts, code sections, or tasks, and explain the rationale behind each action.
- **Hands-On and Iterative:**  
  Encourage students to use LLMs for brainstorming, code generation, and debugging. Provide example prompts and tips for effective prompt engineering.
- **Documentation and Reporting:**  
  Include templates and instructions for summarizing results and writing reports. Emphasize reproducibility, documentation, and good coding practices.
- **Troubleshooting:**  
  Provide a troubleshooting guide tailored to the technical challenges of the workshop (e.g., handling large files, cluster usage, etc.).

---

## 3. Customization for Each Workshop

- Adapt all content to the specific biological or computational challenge of the workshop.
- Update instructions, code scaffolds, and documentation to match the workflow, data types, and tools relevant to the current topic (e.g., large data, cluster computing, new analysis methods).
- Ensure clarity and accessibility for students with little prior computational experience.

---

## 4. Distribution and Usability

- Ensure all files are ready for GitHub Classroom distribution:  
  - Clear file naming and organization  
  - Minimal, well-commented, and easy-to-follow code  
  - Self-contained instructions and documentation
- Double-check that the structure, naming, and content match the pedagogical style and usability of Workshop 1.

---

**Summary:**  
The goal is to create a complete, student-friendly set of workshop materials that guide students through the computational problem-solving process in a hands-on, scaffolded, and supportive manner. The materials should empower students to complete the workshop tasks, learn new skills, and develop confidence in computational biology and bioinformatics.
