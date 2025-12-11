---
title: "AI-Assisted Development Workflow"
sub_title: "Building bioinformatics tools with OpenCode, OpenSpec, and agents"
author: "BU Bioinformatics Graduate Program"
options:
    end_slide_shorthand: true
---

Session 5: AI-Assisted Development Workflow
===

**Learning Objectives:**
- Understand modern AI-assisted development paradigm
- Use OpenCode for code generation and refactoring
- Apply OpenSpec for specification-driven development
- Leverage agents and subagents for specialized tasks
- Build a complete bioinformatics tool end-to-end
- Establish best practices for AI-assisted coding

---

The Development Paradigm Shift
===

**Traditional coding:**
```
Think → Type → Debug → Test → Repeat
```
- You write every line
- You debug every error
- You write documentation

**AI-assisted coding:**
```
Specify → Guide → Validate → Refine → Repeat
```
- AI generates code
- You review and validate
- AI helps debug
- AI generates documentation

**Role change:** From coder to director

---

The AI Coding Landscape
===

**Tools available:**

1. **IDE Assistants**
   - GitHub Copilot
   - Cursor
   - OpenCode ← We'll use this

2. **Standalone Tools**
   - ChatGPT / Claude for code
   - Specialized code models

3. **Code Generation Frameworks**
   - OpenSpec - specification framework
   - Aider - AI pair programmer

**Today: OpenCode + OpenSpec workflow**

---

What is OpenCode?
===

**OpenCode** = Terminal-based AI coding assistant

**Capabilities:**
- Generate code from natural language
- Refactor existing code
- Debug and fix errors
- Write tests
- Generate documentation
- Use specialized subagents
- Execute commands and validate code

**Think:** ChatGPT + Claude + code execution + file system access

---

OpenCode Features
===

**Key features:**

1. **Context awareness** - knows your entire codebase
2. **Agent system** - delegates to specialized subagents
3. **Tool use** - can run commands, read files, search code
4. **Iterative** - refines until working
5. **Interactive** - you guide the process

**Advantage over ChatGPT:** Direct file manipulation + execution

---

OpenCode & MCP Integration
===

**From Session 3:** Model Context Protocol

**OpenCode supports MCP servers:**
- Can use Context7 for documentation lookup
- Can use filesystem servers for controlled access
- Can use any installed MCP server
- Configured via OpenCode settings

**Example use:** While coding, OpenCode can query Context7 MCP for API documentation

---

Configuring MCP in OpenCode
===

**OpenCode MCP configuration:**

```json
// In OpenCode settings/config
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@context7/mcp-server"],
      "env": {
        "CONTEXT7_API_KEY": "your-key"
      }
    }
  }
}
```

**Once configured:**
- OpenCode automatically discovers MCP tools
- Can reference documentation during code generation
- Improves accuracy for library-specific code
- No manual doc lookup needed

---

MCP-Enhanced Development
===

**Scenario:** "Create a pandas data processing function"

**Without MCP:**
```
OpenCode generates code based on training data
May use outdated APIs
Might miss best practices
```

**With Context7 MCP:**
```
OpenCode: "Let me check current pandas docs..."
(Queries Context7 MCP)
OpenCode generates code with:
  - Current API usage
  - Best practices from docs
  - Proper type hints
```

**MCP = Live documentation reference**

---

What is OpenSpec?
===

**OpenSpec** = Specification format for AI code generation

**Purpose:** Bridge human intent and AI implementation

**Structure:**
```yaml
name: My Tool
purpose: What it does
inputs:
  - param1: description
  - param2: description
outputs:
  - output1: description
behavior:
  - Step 1 description
  - Step 2 description
constraints:
  - Requirement 1
  - Requirement 2
```

**Clear specs → Better code**

---

Why Specifications Matter
===

**Without spec:**
```
"Write a tool to analyze sequences"
```
- Ambiguous
- Missing details
- Likely wrong assumptions

**With spec:**
```yaml
name: SequenceAnalyzer
inputs:
  - sequences: List[str], FASTA format DNA sequences
  - min_length: int, filter sequences shorter than this
outputs:
  - stats: Dict with gc_content, length, complexity
behavior:
  - Validate FASTA format
  - Calculate GC content per sequence
  - Compute sequence complexity (Shannon entropy)
  - Return structured results
```

**Precise → Correct implementation**

---

The AI-Assisted Workflow
===

**6-phase development cycle:**

```
1. SPECIFICATION
   Write clear requirements (OpenSpec)
   ↓
2. INITIAL GENERATION
   AI creates first implementation
   ↓
3. VALIDATION
   Run code, check behavior
   ↓
4. REFINEMENT
   Fix bugs, add features
   ↓
5. TESTING
   AI generates tests, validate
   ↓
6. DOCUMENTATION
   AI writes docs, commit
```

**Iterate phases 3-4 until satisfied**

---

Tutorial Project Overview
===

**We'll build:** `variant_annotator` tool

**Functionality:**
- Read VCF file with genomic variants
- Query NCBI for gene information
- Annotate variants with gene context
- Generate summary report

**Incorporates:**
- File I/O
- API integration (tool use)
- Data processing
- Report generation

**Realistic bioinformatics utility**

---

Phase 1: Specification
===

**First, write the spec:**

```yaml
name: VariantAnnotator
version: 1.0.0
purpose: |
  Annotate genomic variants from VCF file with gene
  information from NCBI databases

inputs:
  vcf_file:
    type: str
    description: Path to VCF file with variants
    required: true
  output_format:
    type: str
    description: Output format (json, tsv, html)
    default: json

outputs:
  annotated_variants:
    type: List[Dict]
    description: Variants with gene annotations
    schema:
      - chromosome: str
      - position: int
      - ref: str
      - alt: str
      - gene: str
      - gene_description: str
```

---

Phase 1: Specification (cont.)
===

```yaml
behavior:
  - Parse VCF file to extract variants
  - For each variant:
    - Identify overlapping gene(s) by position
    - Query NCBI Gene database for details
    - Retrieve gene symbol, name, function
  - Compile annotations into structured format
  - Generate output in requested format

constraints:
  - Handle VCF format errors gracefully
  - Rate-limit NCBI API calls (max 3/second)
  - Cache gene queries to avoid redundant API calls
  - Support GRCh37 and GRCh38 reference builds

error_handling:
  - Invalid VCF: Return clear error message
  - NCBI API failure: Retry 3 times, then skip
  - Missing genes: Mark as "intergenic"

dependencies:
  - pysam (VCF parsing)
  - requests (API calls)
  - pandas (data manipulation)
```

---

Why This Spec Works
===

**Good practices demonstrated:**

✅ **Clear purpose** - one sentence summary

✅ **Typed parameters** - types specified

✅ **Detailed behavior** - step-by-step logic

✅ **Constraints** - performance requirements

✅ **Error handling** - failure modes defined

✅ **Dependencies** - explicit libraries

**AI can implement this accurately**

---

Phase 2: OpenCode Generation
===

**OpenCode workflow:**

1. **Launch OpenCode**
```bash
opencode
```

2. **Provide specification**
```
Create a new Python tool based on this specification:
[paste OpenSpec]

Put the code in variant_annotator.py
```

3. **OpenCode generates:**
   - Main script structure
   - Function definitions
   - Error handling
   - Basic tests

---

OpenCode Agent System
===

**OpenCode uses agents internally:**

**Main agent:** Orchestrates the task

**Exploration subagent:**
- Searches codebase
- Finds relevant examples
- Identifies patterns

**Code subagent:**
- Generates implementations
- Refactors code
- Fixes bugs

**Test subagent:**
- Generates test cases
- Validates functionality

**You don't control subagents directly - OpenCode manages them**

---

Phase 3: Validation
===

**Once code generated, validate:**

```bash
# Check syntax
python -m py_compile variant_annotator.py

# Try running
python variant_annotator.py --help

# Test with sample data
python variant_annotator.py test_variants.vcf
```

**OpenCode can do this for you:**
```
Run the script with test_variants.vcf and show me the output
```

**Catches immediate issues**

---

Phase 4: Iterative Refinement
===

**Common issues and fixes:**

**Issue:** "API rate limit exceeded"
```
Add rate limiting to NCBI queries - maximum 3 requests
per second with exponential backoff on errors
```

**Issue:** "VCF parsing fails on multi-allelic sites"
```
Update the VCF parser to handle multi-allelic variants
by splitting them into separate entries
```

**Issue:** "Gene overlaps not detected correctly"
```
The gene overlap logic is wrong. Use NCBI's gene coordinates
API and check for position overlaps including strand
```

---

Using Subagents Explicitly
===

**OpenCode allows explicit subagent delegation:**

**Explore codebase:**
```
Use the exploration subagent to find examples of
VCF parsing in the codebase
```

**Focused refactoring:**
```
Use the code subagent to refactor the NCBI query
function to use connection pooling for better performance
```

**Comprehensive testing:**
```
Use the test subagent to generate pytest tests covering
all edge cases in the VCF parser
```

**Specialization → Better results**

---

Debugging with AI
===

**When errors occur:**

```
❌ Error:
Traceback (most recent call last):
  File "variant_annotator.py", line 45, in parse_vcf
    chrom = record.chrom
AttributeError: 'NoneType' object has no attribute 'chrom'
```

**Ask OpenCode:**
```
Fix this AttributeError in the parse_vcf function.
The error happens when processing variant_annotator.vcf
at line 45. Add proper null checking and error handling.
```

**OpenCode:**
1. Analyzes error
2. Identifies cause
3. Fixes code
4. Adds validation

---

Phase 5: Testing
===

**Generate comprehensive tests:**

```
Generate pytest tests for variant_annotator.py that cover:
1. Valid VCF parsing
2. Invalid VCF format handling
3. NCBI API call mocking
4. Rate limiting behavior
5. Multi-allelic variant handling
6. Output format generation (JSON, TSV, HTML)

Put tests in tests/test_variant_annotator.py
```

**OpenCode generates:**
- Test fixtures
- Mocked API responses
- Edge case coverage
- Assertions

---

Test-Driven Development with AI
===

**Alternatively, write tests first:**

```
I want to build a variant annotator. First, generate
comprehensive pytest tests that specify the expected
behavior based on this spec: [OpenSpec]

Then implement the code to pass those tests.
```

**TDD advantages:**
- Clear requirements
- Guaranteed test coverage
- Behavioral specification

**AI excels at both test generation and implementation**

---

Phase 6: Documentation
===

**Generate docs:**

```
Generate comprehensive documentation for variant_annotator.py
including:
- README.md with installation and usage
- Docstrings for all functions (Google style)
- API documentation for the NCBI integration
- Example usage with sample data
- Troubleshooting section
```

**OpenCode creates:**
- User-friendly README
- API documentation
- Examples
- Inline comments

**Documentation often neglected → AI makes it effortless**

---

Real-Time Tutorial Demo
===

**Live coding session:**

We'll build `variant_annotator` from scratch using OpenCode

**Watch for:**
1. How to write effective prompts
2. When to use subagents
3. Iteration cycles
4. Error recovery
5. Testing integration
6. Documentation generation
7. **Using Context7 MCP for API references** ← NEW

**Interactive - ask questions as we go!**

---

Demo Step 1: Setup
===

**Project initialization:**

```bash
# Create project directory
mkdir variant_annotator_project
cd variant_annotator_project

# Initialize git
git init

# Create spec file
touch variant_annotator.openspec.yaml

# Launch OpenCode
opencode
```

**OpenCode starts with full project context**

---

Demo Step 2: Specification
===

**In OpenCode:**

```
I want to create a bioinformatics tool. First, let me
show you the specification:

[Paste OpenSpec from earlier slides]

Please review this spec and suggest any improvements
or missing details before we implement.
```

**AI reviews and suggests:**
- Missing edge cases
- Additional parameters
- Better error handling
- Performance considerations

**Collaborative specification refinement**

---

Demo Step 3: Initial Implementation
===

**After spec approved:**

```
Based on the approved specification, implement the
variant_annotator tool. Create the following files:

1. variant_annotator.py - main module
2. requirements.txt - dependencies
3. README.md - basic usage docs

Use best practices:
- Type hints
- Error handling
- Logging
- Configuration via arguments
```

**Watch OpenCode work through the implementation**

---

Demo Step 4: Testing
===

**Create test data:**

```
Generate a small test VCF file (test_variants.vcf) with
5 variants covering these cases:
1. Variant in a coding gene
2. Intergenic variant
3. Multi-allelic variant
4. Variant at gene boundary
5. Variant on different chromosomes

Then run the tool on this test file and show me the output.
```

**OpenCode:**
1. Creates test data
2. Runs tool
3. Shows results
4. Identifies issues

---

Demo Step 5: Refinement
===

**Based on test results:**

```
The tool runs but has these issues:
1. Rate limiting not working correctly
2. Multi-allelic handling creates duplicate entries
3. HTML output format is malformed

Please fix these issues one by one, testing after each fix.
```

**Iterative improvement until working correctly**

---

Demo Step 6: Polish
===

**Final touches:**

```
Now that the core functionality works:

1. Add a progress bar for large VCF files (use tqdm)
2. Add summary statistics at the end
3. Generate comprehensive docstrings
4. Create unit tests with mocked NCBI responses
5. Add example usage to README
6. Create a simple CLI with argparse validation
```

**Transform from working to production-ready**

---

Demo Step 7: Using MCP for Documentation
===

**Leverage Context7 MCP during development:**

```
I need to use the pysam library for VCF parsing. Use Context7
to look up the best practices for reading VCF files with pysam,
then implement the parser using those recommendations.
```

**What happens:**
1. OpenCode queries Context7 MCP server
2. Retrieves current pysam VCF documentation
3. Generates code following documented best practices
4. Includes proper error handling from docs

**Result:** More accurate code that follows current library conventions

---

MCP + OpenCode in Practice
===

**Example interaction:**

```
You: "Add CSV export functionality using pandas"

OpenCode (internally):
  1. Queries Context7: "pandas to_csv best practices"
  2. Retrieves docs on encoding, index handling, delimiters
  3. Generates code following documented patterns

You see:
  - Code with proper pandas usage
  - Handles edge cases mentioned in docs
  - Uses recommended parameters
```

**MCP makes OpenCode more accurate without you needing to look up docs**

---

Best Practices for AI-Assisted Coding
===

**DO:**

✅ Write detailed specifications first
✅ Validate each iteration
✅ Be specific in prompts ("use pandas" not "process data")
✅ Configure MCP servers for documentation access
✅ Review AI-generated code carefully
✅ Test thoroughly (AI can miss edge cases)
✅ Use version control (git)
✅ Iterate in small steps

**DON'T:**

❌ Blindly trust generated code
❌ Skip testing
❌ Use vague requirements
❌ Ignore security implications
❌ Forget to review dependencies

---

Prompting Strategies for Code Generation
===

**Effective code prompts:**

**❌ Vague:**
```
"Make a sequence analyzer"
```

**✅ Specific:**
```
"Create a Python function that takes a DNA sequence
string, validates it contains only ATCG, calculates
GC content as a percentage, and returns a dict with
keys 'length', 'gc_content', and 'valid'. Include
error handling and docstring."
```

**Specificity → Accuracy**

---

When AI Coding Works Best
===

**✅ Ideal use cases:**

- Boilerplate code (CLI setup, config parsing)
- Standard implementations (file I/O, API wrappers)
- Test generation
- Documentation
- Code refactoring
- Bug fixing with clear errors
- Translation between languages

**🤔 Requires care:**

- Novel algorithms
- Performance-critical code
- Security-sensitive operations
- Complex business logic

---

When to Write Code Yourself
===

**Don't use AI for:**

1. **Core algorithms** you need to understand deeply
2. **Learning** - AI shortcuts learning
3. **Security-critical** code - needs expert review
4. **Real-time systems** - need guaranteed performance
5. **Novel research code** - AI trained on existing patterns

**AI is a tool, not a replacement for understanding**

---

AI-Assisted vs Traditional Development
===

**Productivity gains:**
- 30-50% faster for standard tasks
- 70%+ faster for documentation/tests
- Comparable speed for novel algorithms

**Quality considerations:**
- Generated code quality varies
- May not follow team conventions
- Can introduce subtle bugs
- Always needs review

**Best approach:** Hybrid - AI for scaffolding, human for critical logic

---

Version Control with AI
===

**Git workflow with AI coding:**

```bash
# Commit before AI changes
git commit -m "Baseline before AI iteration"

# Let AI make changes
# ... OpenCode generates/modifies code ...

# Review changes
git diff

# If good, commit
git add .
git commit -m "Add variant annotation feature (AI-assisted)"

# If bad, revert
git reset --hard HEAD
```

**Frequent commits = easy rollback**

---

Code Review Checklist
===

**Always verify AI-generated code:**

☐ **Correctness** - Does it do what was asked?
☐ **Edge cases** - Handles invalid input?
☐ **Security** - No SQL injection, path traversal, etc.?
☐ **Performance** - Efficient algorithms?
☐ **Dependencies** - Necessary and trustworthy?
☐ **Style** - Follows project conventions?
☐ **Tests** - Adequate coverage?
☐ **Documentation** - Clear and accurate?

**You are responsible for code quality, not the AI**

---

Advanced: Multi-File Projects
===

**OpenCode handles complex projects:**

```
Create a package structure for variant_annotator:

variant_annotator/
  __init__.py
  cli.py          # Command-line interface
  parser.py       # VCF parsing
  annotator.py    # Core annotation logic
  ncbi.py         # NCBI API wrapper
  report.py       # Report generation
  utils.py        # Helper functions
tests/
  test_parser.py
  test_annotator.py
  test_ncbi.py
setup.py
README.md

Implement the package following Python best practices.
```

**Handles architecture and organization**

---

Combining Techniques
===

**Our tool uses everything from this series:**

**Session 1 - Context Engineering:**
- Clear prompts for NCBI queries
- Structured JSON responses

**Session 2 - RAG:**
- Could add: Query protocol database for annotation standards

**Session 3 - Tool Use & MCP:**
- NCBI API integration (direct tools)
- Context7 MCP for documentation
- File operations

**Session 4 - Agents:**
- OpenCode's internal agent system
- Multi-step workflow

**Session 5 - Integration:**
- End-to-end development
- MCP-enhanced code generation

---

Real-World Project Workflow
===

**Typical bioinformatics project:**

```
1. Research question/need identified
   ↓
2. Write specification (OpenSpec)
   ↓
3. Generate initial implementation (OpenCode)
   ↓
4. Validate with test data
   ↓
5. Iterative refinement
   ↓
6. Peer review (human + AI)
   ↓
7. Documentation and testing
   ↓
8. Deploy and monitor
```

**AI accelerates steps 3-7 significantly**

---

Measuring Success
===

**How to evaluate your AI-assisted code:**

**Metrics:**
1. **Correctness** - Does it work?
2. **Time saved** - vs manual coding
3. **Code quality** - Readability, maintainability
4. **Bug rate** - Issues found in testing/production
5. **Learning** - Did you understand the code?

**Goal:** Faster development without sacrificing quality

**Achieved through:** Validation, testing, review

---

Future of AI-Assisted Development
===

**Trends:**

1. **Better context understanding** - Larger context windows
2. **Specialized models** - Biology-specific code models
3. **Autonomous debugging** - AI fixes its own bugs
4. **Natural language interfaces** - Less technical prompting
5. **Formal verification** - AI-provable correctness

**Your advantage:** Learning these skills now

---

Key Takeaways
===

1. **Specifications matter** - Clear specs → Good code
2. **OpenCode** powerful for iterative development
3. **Validate everything** - Never trust AI blindly
4. **Iterate in steps** - Small changes, test frequently
5. **Use agents** strategically for specialized tasks
6. **You're the director** - Guide, don't just accept
7. **Test and document** - AI makes these easier
8. **Combine techniques** - RAG + Tools + Agents = Powerful

---

Paradigm Shift Summary
===

**Old paradigm:**
- Write every line
- Debug everything
- Slow iteration

**New paradigm:**
- Specify intent
- AI generates
- Rapid iteration
- **You validate and guide**

**Your role:** From coder to **architect** and **validator**

**This is the future of software development**

---

Practical Exercises
===

**After this session, try:**

1. **Rebuild tutorial project** from scratch with OpenCode
2. **Add features:** Email reports, visualization, batch processing
3. **New tool:** Pick a bioinformatics task you need automated
4. **Refactor old code:** Use AI to improve existing scripts
5. **Documentation:** AI-generate docs for current projects

**Hands-on practice is essential**

---

Common Questions
===

**Q: "Will AI replace bioinformatics programmers?"**

A: No - it augments, not replaces. Domain knowledge, validation, and critical thinking still essential.

**Q: "Is AI-generated code production-ready?"**

A: Rarely without review. Always validate, test, and review.

**Q: "Should I learn to code if AI can do it?"**

A: Absolutely! You need to understand code to validate it, guide AI, and design solutions.

**Q: "What about licensing of AI code?"**

A: Complex legal area. Your usage typically owns output, but verify with your institution.

---

Resources
===

**Tools:**
- OpenCode: https://opencode.ai
- OpenSpec: [Check OpenCode docs]
- Cursor: https://cursor.sh
- GitHub Copilot: https://github.com/features/copilot

**MCP:**
- Model Context Protocol: https://modelcontextprotocol.io/
- Context7 MCP: https://github.com/context7/mcp-server
- MCP Server List: https://github.com/modelcontextprotocol/servers

**Learning:**
- OpenCode Documentation
- AI-assisted coding best practices
- Prompt engineering for code
- Test-driven development with AI
- MCP integration guides

**Community:**
- OpenCode Discord/forums
- GitHub Copilot patterns
- AI coding communities
- MCP community

---

Final Thoughts
===

**AI-assisted development is:**

✨ **Powerful** - Dramatically faster iteration

⚠️ **Requires skill** - Prompting, validation, architecture

🎯 **Best for** - Scaffolding, boilerplate, documentation

🧠 **Still needs you** - Critical thinking, domain knowledge, validation

**Master this workflow, and you'll be 10x more productive**

**But always remember: You are responsible for the code**

---

Thank You!
===

**Series Recap:**

1. ✅ Context Engineering - Better prompts
2. ✅ RAG - Knowledge retrieval
3. ✅ Tool Use & MCP - Dynamic capabilities + standardization
4. ✅ Agents - Autonomous systems
5. ✅ AI-Assisted Dev - Practical workflow with MCP integration

**You now have the complete toolkit for practical LLM usage in bioinformatics**

**Questions? Discussion? Let's talk!**

---

Course Materials
===

**All materials available:**
- Slides: `lectures/session_[1-5]_*.md`
- Demo code: `lectures/demos/session_[1-5]/`
- Specifications: Example OpenSpec files
- Sample data: Test files for all demos

**Continue learning:**
- Practice with real projects
- Join AI coding communities
- Stay updated (rapid field)

**Good luck with your AI-assisted bioinformatics work!**
