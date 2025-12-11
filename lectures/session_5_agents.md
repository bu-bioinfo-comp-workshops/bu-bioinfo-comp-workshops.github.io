---
title: "AI Agents - Autonomous Reasoning Systems"
sub_title: "Combining RAG, tools, and reasoning for autonomous problem-solving"
author: "BU Bioinformatics Graduate Program"
options:
    end_slide_shorthand: true
---

Session 4: AI Agents
===

**Learning Objectives:**
- Understand what makes an AI agent
- Learn common agent architectures (ReAct, Plan-and-Execute)
- Implement a simple agent loop
- Recognize when agents are appropriate
- Debug and evaluate agent behavior

---

What is an AI Agent?
===

**Simple LLM:** User → LLM → Response (one-shot)

**Agent:** Autonomous system that:
1. **Perceives** its environment
2. **Reasons** about what to do
3. **Acts** using available tools
4. **Repeats** until goal achieved

**Key difference:** Autonomy and iteration

---

The Agent Loop
===

```
┌─────────────────────────────────────┐
│  Goal: Answer user question         │
└───────────┬─────────────────────────┘
            │
            ▼
   ┌────────────────────┐
   │  1. PERCEIVE       │
   │  What's the state? │
   └────────┬───────────┘
            │
            ▼
   ┌────────────────────┐
   │  2. REASON         │
   │  What should I do? │
   └────────┬───────────┘
            │
            ▼
   ┌────────────────────┐
   │  3. ACT            │
   │  Execute action    │
   └────────┬───────────┘
            │
            ▼
      Goal achieved? ──No──┐
            │              │
           Yes             │
            │              │
            ▼              │
         Return ───────────┘
         answer
```

---

Simple Example
===

**User:** "What's the most recent BRCA1 paper?"

**Agent loop:**

**Iteration 1:**
- Perceive: Need to search papers
- Reason: Use search_pubmed tool
- Act: search_pubmed("BRCA1", sort="recent")

**Iteration 2:**
- Perceive: Have PMIDs, need details
- Reason: Fetch most recent abstract
- Act: fetch_abstract(PMID[0])

**Iteration 3:**
- Perceive: Have all needed info
- Reason: Can answer now
- Act: Generate final answer → DONE

---

Why Agents?
===

**Problems agents solve:**

1. **Multi-step tasks** - require planning
2. **Unknown path** - can't predict exact steps
3. **Dynamic decisions** - next step depends on results
4. **Error recovery** - can retry/adapt
5. **Complex goals** - need decomposition

**Example:** "Find genes associated with condition X, get their pathways, and identify common drugs"

---

Agents vs Scripts
===

**Traditional script:**
```python
def analyze():
    data = fetch_data()
    result = process(data)
    return result
```
**Fixed path, no adaptation**

**Agent:**
```python
def agent_loop():
    while not goal_achieved():
        observation = perceive()
        action = reason(observation)
        result = act(action)
        if error: adapt_strategy()
    return final_answer
```
**Dynamic path, adaptive**

---

Agent Architectures
===

**Common patterns:**

1. **ReAct** - Reasoning + Acting
2. **Plan-and-Execute** - Planning first, then execution
3. **Reflection** - Self-critique and improvement
4. **Hierarchical** - Parent agent delegates to sub-agents

We'll focus on **ReAct** (most popular)

---

ReAct Architecture
===

**ReAct** = Reasoning + Acting

**Pattern:**
```
Thought: What do I need to do?
Action: [tool_name, args]
Observation: [tool result]
Thought: What does this mean?
Action: [next tool_name, args]
Observation: [tool result]
...
Thought: I can answer now
Answer: [final response]
```

**Explicit reasoning makes debugging easier**

---

ReAct Example
===

**Question:** "How many exons does BRCA1 have?"

```
Thought: I need gene structure info for BRCA1
Action: search_gene_database("BRCA1")
Observation: {gene_id: 672, ...}

Thought: Got gene ID, now fetch detailed structure
Action: get_gene_structure(672)
Observation: {exons: 24, introns: 23, ...}

Thought: I have the exon count now
Answer: BRCA1 has 24 exons.
```

---

Implementing a Simple Agent
===

```python
def simple_agent(question, tools, max_iterations=5):
    messages = [{"role": "user", "content": question}]
    
    for i in range(max_iterations):
        # LLM reasons about what to do
        response = completion(
            model="anthropic/claude-sonnet-4-20250514",
            messages=messages,
            tools=tools
        )
        
        # Check if done
        if not response.choices[0].message.tool_calls:
            return response.choices[0].message.content
        
        # Execute tools
        for tool_call in response.choices[0].message.tool_calls:
            result = execute_tool(tool_call)
            messages.append({
                "role": "tool",
                "content": str(result),
                "tool_call_id": tool_call.id
            })
    
    return "Max iterations reached"
```

---

State Management
===

**Agents need to track:**
- Conversation history
- Tool results
- Intermediate findings
- Goal status

**Memory types:**

**Short-term:** Current context window
**Long-term:** Database/vector store for past interactions
**Working memory:** Scratchpad for intermediate results

---

Agent Memory Example
===

```python
class AgentMemory:
    def __init__(self):
        self.short_term = []  # Recent messages
        self.working_memory = {}  # Key findings
        self.tool_history = []  # Tool calls made
    
    def add_observation(self, tool_name, result):
        self.short_term.append({
            "tool": tool_name,
            "result": result,
            "timestamp": time.time()
        })
        
    def get_context(self, max_tokens=4000):
        # Return relevant context within token limit
        return self.short_term[-10:]  # Last 10 items
    
    def store_finding(self, key, value):
        self.working_memory[key] = value
```

---

Plan-and-Execute Architecture
===

**Alternative to ReAct:**

**Phase 1: Planning**
```
Goal: Find common pathways for gene set
Plan:
  1. For each gene, query pathway database
  2. Collect all pathways
  3. Find intersection
  4. Rank by gene count
```

**Phase 2: Execution**
```
Execute step 1... ✓
Execute step 2... ✓
Execute step 3... ✓
Execute step 4... ✓
```

**Advantage:** Clear structure
**Disadvantage:** Less adaptive to unexpected results

---

When Plans Fail
===

**Rigid plan:**
```
1. Query database
2. Process results  ← ERROR: No results found
3. Generate report  ← Can't proceed
```

**Adaptive agent (ReAct):**
```
Try query database → No results
Thought: Database may be down, try alternative
Action: Use web search instead
Observation: Found relevant papers
Thought: Can proceed with alternative data
```

**Agents can adapt, scripts cannot**

---

Reflection Pattern
===

**Add self-critique:**

```
Action: search_pubmed("BRCA mutations")
Observation: 50,000 results (too many)

Reflection: Query too broad, need refinement

Action: search_pubmed("BRCA1 pathogenic mutations clinical")
Observation: 2,000 results (manageable)

Reflection: Much better, proceed with these
```

**Agent evaluates own performance**

---

Agent Tools for Bioinformatics
===

**Essential tools:**

1. **Database queries**
   - UniProt, NCBI, Ensembl
   
2. **Literature search**
   - PubMed, bioRxiv

3. **Sequence analysis**
   - BLAST, alignments, motif search

4. **Computation**
   - Calculator, statistics, plotting

5. **Data manipulation**
   - Parse files, convert formats

6. **Knowledge retrieval**
   - RAG over documents/protocols

---

Example: Literature Review Agent
===

**Goal:** "Summarize CRISPR base editing advances in 2024"

**Agent workflow:**

1. Search PubMed("CRISPR base editing", year=2024)
2. Get top 20 paper abstracts
3. Extract key innovations from each
4. Identify common themes
5. Retrieve full methods for novel approaches
6. Synthesize comprehensive summary

**Autonomous multi-step research**

---

Example: Variant Analysis Agent
===

**Goal:** "Is variant chr17:g.43094692G>A pathogenic?"

**Agent workflow:**

1. Parse variant notation
2. Query ClinVar for known entries
3. If unknown, check gnomAD for population frequency
4. Check conservation (PhyloP scores)
5. Predict effect (SIFT, PolyPhen)
6. Search literature for gene + variant
7. Synthesize evidence
8. Provide classification with confidence

**Integrates multiple evidence sources**

---

Agent Limitations
===

**Challenges:**

1. **Reliability** - probabilistic, not deterministic
2. **Cost** - many LLM calls per query
3. **Speed** - slower than direct code
4. **Debugging** - complex reasoning chains
5. **Halting** - may not know when to stop
6. **Hallucination** - can make up tool results

**Agents ≠ production-ready without validation**

---

The Halting Problem
===

**When should an agent stop?**

**Strategies:**

1. **Max iterations** - hard limit
```python
for i in range(max_iterations):
    ...
```

2. **Goal achievement** - explicit completion
```python
if response.content.startswith("FINAL_ANSWER:"):
    return response
```

3. **Cost limit** - token budget
```python
if total_tokens > budget:
    return "Budget exceeded"
```

4. **Time limit** - timeout
```python
with timeout(60):
    agent.run()
```

---

Debugging Agents
===

**Common issues:**

**1. Infinite loops**
- Agent repeats same action
- Solution: Track action history, prevent repeats

**2. Wrong tool selection**
- Misunderstands what tool does
- Solution: Better tool descriptions

**3. Parameter hallucination**
- Makes up tool parameters
- Solution: Stricter schema validation

**4. Premature termination**
- Stops before goal achieved
- Solution: Explicit goal checking

---

Agent Evaluation
===

**How to measure agent success?**

**Metrics:**

1. **Task completion rate** - did it finish?
2. **Accuracy** - is answer correct?
3. **Efficiency** - how many steps/tokens?
4. **Cost** - total API usage
5. **Tool utilization** - used right tools?

**Challenges:**
- Hard to define "correct" for open-ended tasks
- May need human evaluation
- Stochastic behavior (different runs vary)

---

Practical Demo Overview
===

**Demo 1:** Simple ReAct Agent
- Basic agent loop implementation
- Tool selection and execution
- Reasoning trace visualization

**Demo 2:** Literature Research Agent
- Multi-step paper search
- Information aggregation
- Synthesis and summarization

**Demo 3:** Debugging Agent Failures
- Common failure modes
- Adding guardrails
- Recovery strategies

---

Demo 1: ReAct Agent
===

**Components:**
- Agent loop with reasoning
- Multiple tool options
- Explicit thought process
- Termination logic

**Example query:** "Find the chromosomal location of TP53 and identify nearby genes within 1Mb"

**Watch:** How agent plans and executes steps

---

Demo 2: Research Agent
===

**Task:** Autonomous literature review

**Capabilities:**
- Search papers by topic
- Filter by relevance
- Extract key findings
- Synthesize results
- Generate structured report

**Example:** "What are therapeutic strategies for Huntington's disease mentioned in 2023-2024 papers?"

---

Demo 3: Failure Analysis
===

**Demonstrate:**

1. **Infinite loop** - agent repeats failed action
   - Show detection and recovery

2. **Wrong tool** - uses inappropriate tool
   - Show how to improve descriptions

3. **Incomplete answer** - stops too early
   - Show goal validation

**Learn from failures**

---

Key Takeaways
===

1. **Agents = autonomous loops** (perceive, reason, act)
2. **ReAct pattern** explicit reasoning + actions
3. **State management** essential for multi-step tasks
4. **Tools + RAG** give agents capabilities
5. **Reliability < traditional code** (probabilistic)
6. **Debugging requires** reasoning trace inspection
7. **Appropriate for** complex, multi-step, adaptive tasks
8. **Not appropriate for** deterministic, real-time, or safety-critical tasks

---

Theory ↔ Practice Connections
===

**Theory:** LLMs trained on reasoning patterns in text

**Practice:** Explicit "Thought:" prompts activate reasoning

---

**Theory:** Attention processes all context

**Practice:** Agent state/history must fit in context window

---

**Theory:** Autoregressive generation (one token at a time)

**Practice:** Agent decisions are sequential, not globally optimal

---

When to Use Agents
===

**✅ Good for:**
- Research workflows
- Data exploration
- Complex analysis pipelines
- Uncertain problem spaces
- Human-in-the-loop tasks

**❌ Bad for:**
- Production pipelines
- Real-time systems
- Safety-critical operations
- Simple, well-defined tasks
- Cost-sensitive applications

---

Looking Ahead: Session 5
===

**Next topic:** AI-Assisted Development Workflow

**Bringing it all together:**
- Using AI coding assistants (OpenCode)
- Specification-driven development (OpenSpec)
- Agent-based code generation
- Iterative refinement workflows
- Testing and validation
- Real project: building a bioinformatics tool from scratch

**The most practical session yet!**

---

Resources
===

**Papers:**
- "ReAct: Synergizing Reasoning and Acting in Language Models" (Yao et al., 2023)
- "Reflexion: Language Agents with Verbal Reinforcement Learning" (Shinn et al., 2023)
- "Toolformer: Language Models Can Teach Themselves to Use Tools" (Schick et al., 2023)

**Frameworks:**
- LangGraph: https://github.com/langchain-ai/langgraph
- AutoGPT: https://github.com/Significant-Gravitas/AutoGPT
- AgentGPT: https://agentgpt.reworkd.ai/

**Demo code:** `lectures/demos/session_4/`

---

Questions?
===

Next session: **AI-Assisted Development Workflow**

*The grand finale where we build a complete tool using everything we've learned*
