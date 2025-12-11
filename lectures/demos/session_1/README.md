# Session 1: Advanced Context Engineering - Demo Code

This directory contains three interactive demonstrations for Session 1.

## Setup

### Prerequisites
```bash
python -m venv .venv
source .venv/bin/activate
pip install litellm python-dotenv
```

### API Key Configuration
Create a `.env` file in this directory:
```bash
ANTHROPIC_API_KEY=sk-ant-your-key-here
```

Or set environment variable:
```bash
export ANTHROPIC_API_KEY=sk-ant-your-key-here
```

## Demos

### Demo 1: Gene Function Annotation Evolution
**File:** `demo_1_gene_annotation.py`

**What it demonstrates:**
- Evolution from naive prompts to sophisticated structured outputs
- Impact of system prompts
- Value of JSON schema specification
- Power of few-shot learning

**Run:**
```bash
python demo_1_gene_annotation.py
```

**Expected learning:**
- How to iteratively improve prompts
- Why examples outperform descriptions
- Importance of structured outputs for downstream processing

---

### Demo 2: Sequence Motif Classification
**File:** `demo_2_motif_classification.py`

**What it demonstrates:**
- Zero-shot vs few-shot classification
- Domain-specific terminology acquisition through examples
- Consistent formatting through pattern matching

**Run:**
```bash
python demo_2_motif_classification.py
```

**Expected learning:**
- When few-shot learning is essential
- How examples teach style and detail level
- Biological context incorporation

---

### Demo 3: Literature Data Extraction
**File:** `demo_3_literature_extraction.py`

**What it demonstrates:**
- Chain-of-thought prompting for complex extraction
- Handling multiple fields and nested JSON
- Batch processing of similar documents
- Graceful handling of missing information

**Run:**
```bash
python demo_3_literature_extraction.py
```

**Expected learning:**
- When to use chain-of-thought reasoning
- Structured extraction from unstructured text
- Systematic review automation potential

---

## Key Concepts Demonstrated

### 1. System Prompts
Set consistent behavior and expertise level across all interactions.

### 2. Few-Shot Learning
Provide 2-5 examples of desired input/output pairs to teach the model your specific needs.

### 3. Chain-of-Thought
Request explicit reasoning steps for complex tasks requiring multi-step logic.

### 4. Structured Output
Always prefer JSON/XML over free text for programmatic downstream processing.

### 5. Iteration
Prompting is experimental - always test and refine based on results.

---

## Exercises for Students

### Exercise 1: Improve Gene Annotation
Modify `demo_1_gene_annotation.py` to include:
- Additional fields (protein domains, tissue expression)
- Multiple database cross-references
- Confidence scores for each field

### Exercise 2: New Motif Types
Extend `demo_2_motif_classification.py` to classify:
- RNA binding motifs
- Protein binding sites  
- Epigenetic marks

### Exercise 3: Full Abstract Parser
Build on `demo_3_literature_extraction.py` to extract:
- Methods details
- Statistical results
- Cited references
- Author affiliations

---

## Troubleshooting

**JSON parsing fails:**
- Check if model wrapped JSON in markdown code fences (```json...```)
- Verify schema matches request
- Try more specific format examples

**Inconsistent results:**
- Add more few-shot examples
- Lower temperature parameter (more deterministic)
- Be more explicit in instructions

**Token limits exceeded:**
- Reduce number of examples
- Shorten system prompt
- Process in batches

---

## Additional Resources

- [Anthropic Prompt Engineering Guide](https://docs.anthropic.com/claude/docs/prompt-engineering)
- [OpenAI Best Practices](https://platform.openai.com/docs/guides/prompt-engineering)
- Chain-of-Thought paper: Wei et al., 2022
