# Computational Workshop Generator

## Purpose

This repository provides a framework and materials for hands-on computational workshops designed for biologists and bioinformaticians with little prior computational experience. The goal is to equip participants with practical skills in computational tools, workflows, and best practices required for modern bioinformatics and computational biology research.

## Content

- **Workshop Materials:**
  - Each workshop is organized as a self-contained module, focusing on realistic, research-driven use cases.
  - Materials include workshop descriptions, instructions, introduction/background slides, and hands-on exercises.
  - Topics covered: Linux basics, command line navigation, cluster computing, version control, workflow management, programming (Python, R, Bash), and use of large language models (LLMs) for code generation and debugging.

- **Problem-Driven Approach:**
  - Workshops follow the cycle: Problem → Prompt → Code → Debug → Result → Iterate → Add Features.
  - Participants learn by iteratively solving real-world problems with LLMs and computational tools.

- **Repository Structure:**
  - `workshop_N/` directories: Each workshop has its own folder with description, LLM prompt, instructions, and slides.
  - Example: `workshop_1/`, `workshop_1_description.md`, `workshop_1_instructions.md`, etc.
  - Supporting scripts and external materials (e.g., scraping scripts, data) are organized in relevant subdirectories.

- **External Materials:**
  - Scripts for gathering and processing external resources (e.g., web scraping for RAG applications) are included where relevant.
  - Example: A web scraping script for BU SCC documentation, with output JSONs stored in `external_materials/scc/scraped_pages/` (ignored by git).

## Strategy

- **Hands-On, Iterative Learning:**
  - Workshops are structured around realistic challenges, encouraging participants to iteratively prompt LLMs, generate and debug code, and add new features.
  - Emphasis is placed on learning by doing, with immediate feedback and opportunities to troubleshoot and extend solutions.

- **Self-Contained Modules:**
  - Each workshop builds on previous skills but is designed to be approachable for newcomers.
  - All required materials and instructions are provided within each module.

- **Reproducibility and Collaboration:**
  - Materials are distributed via GitHub Classroom, enabling easy access, version control, and collaboration.
  - Dependency management and environment setup instructions are provided to ensure reproducibility.

## Getting Started

1. Clone the repository.
2. Review the `workshop_N/` folders for workshop-specific materials and instructions.
3. Set up your Python environment (see `requirements.txt` if provided) for any scripts or computational exercises.
4. Follow the instructions and slides in each workshop to begin learning and practicing computational skills.

For questions or contributions, please open an issue or submit a pull request.
