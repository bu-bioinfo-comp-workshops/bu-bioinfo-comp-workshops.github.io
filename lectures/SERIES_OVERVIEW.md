# Practical LLM Usage in Bioinformatics - 6-Session Series

## Overview

This series provides comprehensive training on practical LLM applications for bioinformatics graduate students. The series starts with foundational understanding of LLMs, then progresses through practical implementation techniques, culminating in production-ready AI-assisted development workflows. Each session combines theory with hands-on demonstrations, focusing on how theoretical concepts inform practical implementation.

## Target Audience

Graduate students in bioinformatics who:
- Can code (Python proficiency expected)
- Want to understand LLM fundamentals and practical applications
- Want to integrate LLM capabilities into their research workflows
- Need practical, applicable skills (not just conceptual knowledge)

## Session Structure

Each session follows a consistent format:
- **5 min**: Recap + Learning objectives
- **15 min**: Theory/concepts with visuals
- **20 min**: Live demonstrations with code
- **5 min**: Key takeaways + Q&A

**Time breakdown optimized for:**
- Enough theory to understand "why"
- Enough practice to learn "how"
- Interactive demos that can be paused for questions

---

## Session 0: Practical LLM Primer

**File:** `session_0_practical_llm_primer.md`

### Learning Objectives
- Understand what large language models are and how they work
- Learn about tokens, embeddings, and the attention mechanism
- Understand context windows and their importance
- Learn about prompting and context engineering basics
- Connect theoretical concepts to practical usage

### Key Concepts
- LLM architecture and components
- Tokenization and vocabulary
- Embeddings and vector representations
- Attention mechanism
- Training vs inference
- Foundation models and fine-tuning
- Context windows and memory
- Prompts and prompt engineering basics

### Practical Applications
- Understanding model capabilities and limitations
- Token counting and context optimization
- Basic prompt design
- Foundation for all subsequent sessions

---

## Session 1: Coding with LLMs

**File:** `session_1_coding_w_llms.md`

### Learning Objectives
- Understand how to interface with LLMs programmatically via APIs
- Learn about API keys and authentication
- Use Python libraries (litellm) to make LLM calls
- Integrate LLM capabilities into bioinformatics workflows
- Set up development environments for LLM-powered applications

### Key Concepts
- API fundamentals and endpoints
- Authentication and API keys
- JSON request/response format
- litellm library for unified API access
- Environment variable management (.env files)
- Token usage and cost tracking

### Demonstrations
1. **API Setup** - Generating and configuring API keys
2. **Basic LLM Call** - Using litellm to query Claude
3. **Response Parsing** - Extracting information from LLM responses

### Practical Applications
- Programmatic LLM access
- Building LLM-powered scripts
- Integrating LLMs into pipelines
- Understanding API responses and metadata

---

## Session 2: Advanced Context Engineering & Prompt Patterns

**File:** `session_2_context_engineering.md`

### Learning Objectives
- Understand advanced prompt engineering techniques
- Apply few-shot learning to biological problems
- Generate structured outputs (JSON/XML)
- Optimize context usage within token limits
- Debug and iterate on prompts systematically

### Key Concepts
- System prompts vs user prompts (strategic design)
- Few-shot learning (2-5 examples for pattern matching)
- Chain-of-thought prompting (explicit reasoning)
- Structured output generation (JSON schemas)
- Context window optimization
- Token economics and efficiency
- Prompt iteration cycles

### Demonstrations
1. **Gene Function Annotation** - Evolution from naive to sophisticated prompts
2. **Sequence Motif Classification** - Zero-shot vs few-shot comparison
3. **Literature Data Extraction** - Chain-of-thought for complex extraction

### Practical Applications
- Gene annotation with consistent formatting
- Regulatory motif classification
- Automated literature data extraction
- Protocol standardization

### Demo Code Location
`lectures/demos/session_2/`
- `demo_1_gene_annotation.py`
- `demo_2_motif_classification.py`
- `demo_3_literature_extraction.py`
- `README.md`

---

## Session 3: Retrieval-Augmented Generation (RAG)

**File:** `session_3_rag.md`

### Learning Objectives
- Understand when and why to use RAG
- Learn the RAG pipeline architecture
- Implement semantic search with embeddings
- Apply chunking strategies for scientific documents
- Build a simple RAG system for bioinformatics

### Key Concepts
- RAG pipeline: Index → Retrieve → Augment → Generate
- Embeddings for semantic similarity
- Vector databases (ChromaDB, FAISS, Pinecone)
- Document chunking strategies
- Hybrid retrieval (semantic + keyword)
- Metadata filtering
- Reranking for quality

### Demonstrations
1. **Paper Q&A System** - Query genomics research papers
2. **Protocol Search** - Hybrid search with metadata filtering

### Practical Applications
- Literature review automation
- Protocol and methods retrieval
- Genomic annotation lookup
- Lab notebook search
- Documentation Q&A systems

### Demo Code Location
`lectures/demos/session_3/`
- `demo_1_paper_qa.py`
- `README.md`

### Dependencies
```bash
pip install litellm chromadb sentence-transformers python-dotenv
```

---

## Session 4: Tool Use, Function Calling & Model Context Protocol (MCP)

**File:** `session_4_tool_use.md` (Extended session: ~60 minutes)

### Learning Objectives
- Understand the tool-use paradigm for LLMs
- Learn function calling mechanics and schema design
- Understand Model Context Protocol (MCP) architecture
- Use existing MCP servers for tool integration
- Compare direct tools vs MCP approach
- Handle multi-step tool composition

### Key Concepts
- Tool use paradigm (LLM as orchestrator)
- JSON Schema for tool definition
- Function calling mechanics
- **Model Context Protocol (MCP)**
  - MCP architecture (client-server model)
  - MCP vs direct tools comparison
  - Using existing MCP servers
  - Security and permissions model
- Multi-step and parallel tool calls
- NCBI E-utilities integration
- Error handling and recovery
- Security considerations

### Demonstrations
1. **NCBI Gene Info Tool** - Direct tool with E-utilities API
2. **Context7 MCP Server** - Using MCP for documentation lookup
3. **Comparison Demo** - Direct tools vs MCP approach

### Practical Applications
- Database queries (NCBI, UniProt, Ensembl) - direct tools
- Documentation search (Context7) - MCP
- Literature search automation
- Sequence analysis pipelines
- File system access - MCP
- Statistical computations

### Demo Code Location
`lectures/demos/session_4/`
- `demo_1_ncbi_gene_info.py`
- `demo_2_pubmed_search.py`
- `demo_3_mixed_tools.py`
- `README.md`

---

## Session 5: AI Agents - Autonomous Reasoning Systems

**File:** `session_5_agents.md`

### Learning Objectives
- Understand what makes an AI agent
- Learn common agent architectures (ReAct, Plan-and-Execute)
- Implement a simple agent loop
- Recognize when agents are appropriate
- Debug and evaluate agent behavior

### Key Concepts
- Agent definition: Perceive → Reason → Act loop
- ReAct architecture (Reasoning + Acting)
- Plan-and-Execute pattern
- Reflection and self-critique
- State management and memory
- The halting problem
- Agent limitations and reliability

### Demonstrations
1. **Simple ReAct Agent** - Basic agent loop with reasoning trace
2. **Literature Research Agent** - Multi-step autonomous research
3. **Debugging Agent Failures** - Common failure modes and recovery

### Practical Applications
- Automated literature reviews
- Multi-step variant analysis
- Complex data exploration
- Research workflow automation
- Hypothesis generation

### Demo Code Location
`lectures/demos/session_5/`
- `demo_1_react_agent.py`
- `demo_2_research_agent.py`
- `demo_3_debugging_agents.py`
- `README.md`

---

## Session 6: AI-Assisted Development Workflow

**File:** `session_6_ai_assisted_development.md`

### Learning Objectives
- Understand modern AI-assisted development paradigm
- Use OpenCode for code generation and refactoring
- Apply OpenSpec for specification-driven development
- Leverage agents and subagents for specialized tasks
- Build a complete bioinformatics tool end-to-end
- Establish best practices for AI-assisted coding

### Key Concepts
- Development paradigm shift (coder → director)
- OpenCode capabilities and features
- **OpenCode MCP integration** (Context7 for documentation)
- OpenSpec specification format
- 6-phase development cycle
- Agent and subagent usage
- MCP-enhanced code generation
- Code validation and review
- Version control with AI
- When to use AI vs manual coding

### Live Tutorial Project
**Building `variant_annotator`:**
- Read VCF files
- Query NCBI for gene information
- Annotate variants with gene context
- Generate summary reports

**Demonstrates full workflow:**
1. Specification (OpenSpec)
2. Initial generation (OpenCode)
3. Validation (testing)
4. Refinement (iteration)
5. Testing (comprehensive)
6. Documentation (automated)

### Practical Applications
- Rapid prototyping of analysis tools
- Code refactoring and optimization
- Test generation
- Documentation automation
- Bug fixing and debugging
- Boilerplate code generation

### Demo Code Location
`lectures/demos/session_6/`
- `variant_annotator.openspec.yaml` (specification)
- `variant_annotator/` (generated package)
- `TUTORIAL.md` (step-by-step guide)

---

## Technology Stack

### Required Software
- Python 3.8+ (with venv)
- Git
- OpenCode (for Session 5)
- Terminal/command line access

### Python Libraries
```bash
# Core dependencies (all sessions)
pip install litellm python-dotenv

# Session 2 (RAG)
pip install chromadb sentence-transformers

# Session 3-4 (Tools/Agents)
pip install requests biopython pandas

# Session 5 (Development)
pip install pytest black mypy
```

### API Keys Required
- Anthropic API key (Claude models)
- OpenAI API key (optional, for embeddings)

Store in `.env` file:
```bash
ANTHROPIC_API_KEY=sk-ant-your-key-here
OPENAI_API_KEY=sk-your-key-here  # optional
```

---

## Learning Progression

### Session Dependencies
```
Session 0: LLM Primer (foundation)
         ↓
Session 1: Coding with LLMs (API access)
         ↓
Session 2: Context Engineering (advanced prompting)
         ↓
Session 3: RAG ────────────┐
         ↓                 │
Session 4: Tool Use ───────┤
         ↓                 │
Session 5: Agents ─────────┤
         ↓                 │
Session 6: Integration ────┘
    (uses all concepts)
```

### Skill Building
- **Session 0:** Understand foundations (LLM theory)
- **Session 1:** Interface with LLMs (API programming)
- **Session 2:** Master the basics (advanced prompting)
- **Session 3:** Extend capabilities (knowledge retrieval)
- **Session 4:** Add dynamic actions (tools and MCP)
- **Session 5:** Autonomous operation (agent loops)
- **Session 6:** Production workflows (real development)

---

## Bioinformatics Focus Areas

### Genomics
- Variant annotation and interpretation
- Sequence analysis and motif detection
- Gene function annotation
- Pathway analysis

### Literature & Knowledge
- PubMed search and retrieval
- Abstract data extraction
- Literature synthesis
- Protocol search and retrieval

### Data Integration
- NCBI E-utilities (Gene, PubMed, Nucleotide)
- UniProt API
- Database queries
- Multi-source data aggregation

### Tools & Workflows
- Analysis pipeline automation
- Report generation
- Data format conversion
- Experimental protocol assistance

---

## Best Practices Emphasized

### Throughout Series
1. **Always validate** - Never trust LLM output blindly
2. **Iterate incrementally** - Small steps, test frequently
3. **Be specific** - Detailed prompts/specs → better results
4. **Understand the code** - Don't just copy/paste
5. **Version control** - Use git for AI-generated code
6. **Test thoroughly** - AI can miss edge cases
7. **Review for security** - Validate external inputs
8. **Document intent** - Specs and comments matter

### Code Quality
- Type hints for clarity
- Error handling for robustness
- Logging for debugging
- Testing for reliability
- Documentation for maintainability

---

## Common Pitfalls & Solutions

### Session 1 (Prompting)
- **Pitfall:** Vague prompts → inconsistent results
- **Solution:** Use few-shot examples and structured output

### Session 2 (RAG)
- **Pitfall:** Poor chunking → bad retrieval
- **Solution:** Section-based chunking for papers

### Session 3 (Tools)
- **Pitfall:** Inadequate error handling → crashes
- **Solution:** Return errors to LLM for recovery

### Session 4 (Agents)
- **Pitfall:** Infinite loops → wasted tokens
- **Solution:** Max iteration limits and goal checking

### Session 5 (Development)
- **Pitfall:** Accepting code without review → bugs
- **Solution:** Systematic validation checklist

---

## Assessment & Exercises

### After Each Session
Students should be able to:

**Session 0:**
- Explain how LLMs work at a conceptual level
- Understand tokens, embeddings, and attention
- Recognize context window constraints
- Write basic prompts

**Session 1:**
- Set up API keys and authentication
- Make LLM API calls using litellm
- Parse and use LLM responses
- Integrate LLMs into Python scripts

**Session 2:**
- Write effective system and user prompts
- Implement few-shot learning for domain tasks
- Generate and parse structured JSON outputs

**Session 3:**
- Build a simple RAG system for documents
- Choose appropriate chunking strategies
- Query vector databases effectively

**Session 4:**
- Define tool schemas for bioinformatics APIs
- Use existing MCP servers
- Implement multi-step tool workflows
- Handle tool errors gracefully

**Session 5:**
- Implement a basic ReAct agent
- Debug agent reasoning traces
- Decide when agents are appropriate

**Session 6:**
- Write clear specifications (OpenSpec)
- Use OpenCode for complete project development
- Validate and test AI-generated code

### Suggested Projects
1. Protocol search engine (RAG)
2. Variant interpretation assistant (Tools + Agents)
3. Literature review automation (All techniques)
4. Custom analysis pipeline (Full workflow)

---

## Resources & Further Learning

### Official Documentation
- OpenCode: https://opencode.ai/docs
- Anthropic Claude: https://docs.anthropic.com/
- litellm: https://docs.litellm.ai/

### Research Papers
- ReAct (Yao et al., 2023)
- RAG (Lewis et al., 2020)
- Chain-of-Thought (Wei et al., 2022)
- Toolformer (Schick et al., 2023)

### Bioinformatics APIs
- NCBI E-utilities: https://www.ncbi.nlm.nih.gov/books/NBK25501/
- UniProt API: https://www.uniprot.org/help/api
- Ensembl REST API: https://rest.ensembl.org/

### Community
- OpenCode community forums
- Bioinformatics Stack Exchange
- GitHub repositories with example code

---

## Instructor Notes

### Preparation Checklist
- [ ] API keys configured and tested
- [ ] Demo code runs successfully
- [ ] Sample data files prepared
- [ ] OpenCode installed and configured
- [ ] Backup internet connection (for API calls)
- [ ] Screen recording setup (for later review)

### Timing Management
- Stick to 45-minute limit
- Can skip "backup" slides if time runs short
- Prioritize demos over additional theory
- Take questions but don't derail flow
- Provide extra materials for self-study

### Interactive Elements
- Pause demos for questions
- Live prompting (show failures too!)
- Ask students to predict outcomes
- Encourage experimentation
- Share common mistakes

### Equipment Needs
- Projector/screen for slides
- Terminal visible to audience
- Internet connection for API calls
- Microphone for recording (optional)

---

## Questions for Instructor Review

**Questions noted during development:**

1. **OpenSpec integration:** The current materials reference OpenSpec conceptually. Should we create actual OpenSpec validator/tooling, or is the YAML format sufficient for teaching purposes?

2. **API costs:** Materials currently assume budget isn't a concern. Should we add a section on cost optimization and using open-source local models?

3. **Domain specificity:** Examples focus on genomics/molecular biology. Should we add examples from other bioinformatics domains (proteomics, phylogenetics, etc.)?

4. **Data sources:** Should we provide pre-downloaded sample datasets, or have students download during demos (more realistic but riskier)?

5. **Advanced topics:** Consider adding "bonus" materials on:
   - Fine-tuning for domain-specific tasks
   - Prompt caching for cost reduction
   - Multi-modal models (handling figures/images)
   - Local LLM deployment

---

## Version History

**v1.0 - Initial Release**
- 5 comprehensive sessions created
- Presenterm slide format
- Demo code with bioinformatics focus
- Progressive skill building
- Theory ↔ Practice emphasis

**Planned Updates:**
- Additional demo code for Sessions 3-5
- Video recordings of demos
- Extended exercises
- Cost optimization section
- Local model alternatives

---

## License & Usage

These materials were created for the BU Bioinformatics Graduate Program.

**Recommended citation:**
```
BU Bioinformatics Practical LLM Workshop Series (2025)
Sessions 1-5: Context Engineering through AI-Assisted Development
```

---

## Contact & Support

For questions or issues with these materials:
- Check demo code README files
- Review troubleshooting sections in slides
- Consult official tool documentation
- Reach out to course instructors

**Good luck with your AI-assisted bioinformatics work!**
