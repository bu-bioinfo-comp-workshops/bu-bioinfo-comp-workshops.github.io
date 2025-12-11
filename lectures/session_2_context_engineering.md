---
title: "Advanced Context Engineering & Prompt Patterns"
sub_title: "Mastering the art of crafting effective prompts for bioinformatics"
author: "BU Bioinformatics Graduate Program"
options:
    end_slide_shorthand: true
---

Session 2: Advanced Context Engineering
===

**Learning Objectives:**
- Understand advanced prompt engineering techniques
- Apply few-shot learning to biological problems  
- Generate structured outputs (JSON/XML)
- Optimize context usage within token limits
- Debug and iterate on prompts systematically

---

Recap: What is Context?
===

From Session 0 (Practical LLM Primer):

- **Context** = the text input that the LLM processes
- **Context window** = the *N* tokens currently visible to the model
- **Attention mechanism** = how the model uses all context to make predictions

**Key insight:** Everything in the context window influences the output

---

Beyond Basic Prompts
===

Basic prompt:
```
Annotate this sequence: ATCGATCG
```

Problems:
- Ambiguous task (what kind of annotation?)
- No format specification
- No examples of desired output
- Missing biological context

---

System Prompts: Setting Behavior
===

**System prompt** = instructions that set the LLM's role and behavior

```python
system_prompt = {
    "role": "system",
    "content": ("You are an expert molecular biologist "
                "specializing in gene annotation. You provide "
                "detailed, accurate information based on current "
                "genomic databases.")
}
```

System prompts are "sticky" - they influence all subsequent responses

---

System Prompt Design Principles
===

**DO:**
- Be specific about expertise domain
- Define expected behavior clearly
- Set output format expectations
- Provide relevant constraints

**DON'T:**
- Be overly verbose (wastes tokens)
- Include task-specific details (those go in user prompt)
- Contradict yourself

---

Few-Shot Learning
===

**Few-shot learning** = providing examples in the prompt

Why it works:
- The attention mechanism learns patterns from examples
- More effective than lengthy descriptions
- Shows desired format and style

**Tradeoff:** Uses more tokens but increases accuracy

---

Few-Shot Example: Variant Classification
===

```python
user_prompt = """
Classify variants as benign, pathogenic, or VUS.

Examples:
Input: BRCA1 c.5266dupC (p.Gln1756Profs*74)
Output: {"variant": "BRCA1 c.5266dupC", 
         "classification": "pathogenic",
         "reasoning": "Frameshift leading to truncation"}

Input: TP53 c.215C>G (p.Pro72Arg)  
Output: {"variant": "TP53 c.215C>G",
         "classification": "benign",
         "reasoning": "Common polymorphism, no functional impact"}

Now classify:
Input: CFTR c.350G>A (p.Arg117His)
Output:
"""
```

---

Zero-Shot vs Few-Shot vs Many-Shot
===

- **Zero-shot**: No examples, just instructions
- **Few-shot**: 2-5 examples (most common)
- **Many-shot**: 10+ examples (if you have tokens to spare)

**Rule of thumb:** Start with zero-shot, add examples if accuracy is insufficient

---

Chain-of-Thought (CoT) Prompting
===

**Chain-of-Thought** = asking the model to show its reasoning

Standard prompt:
```
Is this mutation likely pathogenic? 
Mutation: ATM c.5762-1G>A
```

CoT prompt:
```
Is this mutation likely pathogenic? Let's think step by step:
1. What is the mutation type?
2. Where is it located?
3. What is known about this gene?
4. What does the literature say?

Mutation: ATM c.5762-1G>A
```

---

Why Chain-of-Thought Works
===

**Theory:** 

The attention mechanism needs intermediate tokens to "work with"

More tokens → more computation → better answers for complex reasoning

**Practice:**

CoT significantly improves accuracy on multi-step problems

Tradeoff: Uses more tokens and takes longer

---

CoT in Bioinformatics
===

Great for:
- Variant interpretation (multiple evidence sources)
- Experimental design (sequential decisions)
- Literature synthesis (multi-document reasoning)
- Pathway analysis (multi-step biochemical reasoning)

Less useful for:
- Simple lookups
- Format conversions
- Single-step classifications

---

Structured Output Generation
===

**Problem:** LLMs generate free text, but we often need structured data

**Solution:** Request specific formats (JSON, XML, tables)

Benefits:
- Easy to parse programmatically
- Reduces ambiguity
- Enables downstream processing

---

JSON Output Example
===

```python
user_prompt = """
Extract gene information from this text and return as JSON.

Text: "The TP53 gene on chromosome 17p13.1 encodes 
a 393 amino acid tumor suppressor protein involved 
in cell cycle regulation."

Return format:
{
  "gene_symbol": "...",
  "chromosome": "...",
  "location": "...",
  "protein_length": ...,
  "function": "..."
}
"""
```

---

Enforcing Structure: JSON Schema
===

Some APIs support JSON schema to guarantee format:

```python
from litellm import completion

schema = {
    "type": "object",
    "properties": {
        "gene_symbol": {"type": "string"},
        "chromosome": {"type": "string"},
        "protein_length": {"type": "integer"},
        "function": {"type": "string"}
    },
    "required": ["gene_symbol", "chromosome"]
}

response = completion(
    model="anthropic/claude-sonnet-4-20250514",
    messages=[{"role": "user", "content": prompt}],
    response_format={"type": "json_schema", "schema": schema}
)
```

---

Context Optimization
===

**Challenge:** Context windows have limits (e.g., 4K, 8K, 128K tokens)

**Strategies:**
1. Prioritize relevant information
2. Summarize background information
3. Use external retrieval (→ Session 2: RAG)
4. Break into multiple calls
5. Remove redundancy

---

Token Economics
===

Most APIs charge by token:
- Input tokens (cheaper)
- Output tokens (more expensive)
- Cached tokens (cheapest)

**Example costs (approximate):**
- Claude Sonnet: $3 per million input tokens
- 1000 tokens ≈ 750 words
- A typical research paper abstract: ~300 tokens

**Lesson:** Be precise but not verbose

---

Context Window Strategy
===

For a 128K token window:

```
System prompt:     ~500 tokens   (0.4%)
Few-shot examples: ~2000 tokens  (1.6%)  
Background data:   ~50000 tokens (39%)
User query:        ~500 tokens   (0.4%)
Response space:    ~75000 tokens (58.6%)
```

Leave room for the response!

---

Common Pitfalls
===

1. **Contradictory instructions**
   - System says "be brief", user says "provide detailed explanation"

2. **Ambiguous tasks**
   - "Analyze this sequence" (analyze how?)

3. **Missing context**
   - Assuming the model knows your specific dataset/organism

4. **Over-constraining**
   - Too many rules can confuse the model

---

Debugging Prompts
===

When outputs are wrong:

1. **Check for ambiguity** - could a human interpret it differently?
2. **Inspect token usage** - are you hitting limits?
3. **Test incrementally** - add complexity gradually
4. **Use temperature** - lower = more deterministic
5. **Try examples** - few-shot often fixes issues
6. **Examine attention** - is important info at the start or end?

---

The Prompt Iteration Cycle
===

```
1. Write initial prompt
   ↓
2. Test on examples
   ↓
3. Identify failure modes
   ↓
4. Refine prompt (add examples, clarify, restructure)
   ↓
5. Test again
   ↓
6. Repeat until satisfactory
```

**Remember:** Prompting is empirical, not theoretical

---

Practical Demo Overview
===

We'll work through three examples:

1. **Basic → Advanced:** Gene function annotation
2. **Few-Shot Learning:** Sequence motif classification  
3. **Structured Output:** Literature data extraction

Let's see theory in practice!

---

Demo 1: Gene Function Annotation
===

**Task:** Given a gene symbol, provide functional annotation

**Iterations:**
- v1: Naive prompt
- v2: With system prompt
- v3: With structured output
- v4: With few-shot examples

Let's see the evolution...

---

Demo 2: Sequence Motif Classification
===

**Task:** Classify DNA motifs by regulatory function

**Challenge:** 
- Requires domain knowledge
- Multiple possible answers
- Needs consistent formatting

**Approach:** Use few-shot learning with biological examples

---

Demo 3: Literature Data Extraction
===

**Task:** Extract structured data from PubMed abstracts

**Requirements:**
- JSON output
- Handle missing fields
- Maintain accuracy

**Technique:** Chain-of-thought + JSON schema

---

Key Takeaways
===

1. **System prompts** set consistent behavior across interactions
2. **Few-shot learning** is your most powerful tool for accuracy
3. **Chain-of-thought** helps with complex, multi-step reasoning
4. **Structured outputs** enable programmatic downstream processing
5. **Context optimization** balances completeness and token economy
6. **Iteration** is essential - prompting is experimental

---

Theory ↔ Practice Connections
===

**Theory:** Attention mechanism weighs all tokens in context

**Practice:** Prompt structure and order matter significantly

---

**Theory:** Context windows are finite (*N* tokens)

**Practice:** Strategic information prioritization is crucial

---

**Theory:** LLMs are trained on next-token prediction

**Practice:** Examples (few-shot) leverage this training directly

---

Looking Ahead: Session 3
===

**Next topic:** Retrieval-Augmented Generation (RAG)

**The problem we'll solve:**

What if your knowledge doesn't fit in the context window?

What if the model wasn't trained on your specific data?

**Solution:** Retrieve relevant information dynamically and augment the context

---

Resources
===

**Practice datasets:**
- NCBI Gene database
- UniProt entries  
- PubMed abstracts
- Sample genomic annotations (in demo code)

**Further reading:**
- "Chain-of-Thought Prompting Elicits Reasoning in LLMs" (Wei et al., 2022)
- Anthropic prompt engineering guide
- OpenAI prompt engineering guide

---

Questions?
===

Next session: **Retrieval-Augmented Generation (RAG)**

Demo code available in: `lectures/demos/session_2/`
