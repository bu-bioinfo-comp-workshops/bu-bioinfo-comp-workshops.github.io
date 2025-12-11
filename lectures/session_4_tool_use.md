---
title: "Tool Use, Function Calling & MCP"
sub_title: "Extending LLM capabilities with external tools and standardized protocols"
author: "BU Bioinformatics Graduate Program"
options:
    end_slide_shorthand: true
---

Session 4: Tool Use & MCP
===

**Learning Objectives:**
- Understand the tool-use paradigm for LLMs
- Learn function calling mechanics and schema design
- Understand Model Context Protocol (MCP) architecture
- Use existing MCP servers for tool integration
- Compare direct tools vs MCP approach
- Handle multi-step tool composition

**Extended session:** ~60 minutes (includes MCP content)

---

Recap: RAG vs Tools
===

**Session 3 - RAG:**
- Retrieves static documents
- Good for: knowledge bases, papers, protocols

**Today - Tools:**
- Execute dynamic operations
- Good for: databases, calculations, real-time data

**Also today - MCP:**
- Standardized protocol for tools
- Good for: reusability, security, community sharing

---

The Limits of Pure Generation
===

LLMs are great at:
- Text generation
- Pattern recognition
- Reasoning with provided information

LLMs are terrible at:
- Precise calculations (342 × 871 = ?)
- Current information (today's weather)
- Database queries (how many samples in DB?)
- Running code/commands

**Solution:** Let LLMs orchestrate, tools execute

---

Session Roadmap
===

**Part 1: Direct Tool Integration (30 min)**
- Function calling basics
- JSON Schema
- Direct implementation
- NCBI API example

**Part 2: Model Context Protocol (25 min)**
- MCP architecture
- Using existing MCP servers
- MCP vs direct tools
- Context7 MCP demo

**Part 3: Best Practices (5 min)**
- When to use which approach
- Error handling
- Security

---

# Part 1: Direct Tool Integration

---

What is Tool Use?
===

**Tool use** = LLM can request external function execution

**Flow:**
1. User asks question requiring external data/computation
2. LLM recognizes it needs a tool
3. LLM generates structured tool call request
4. System executes the tool
5. Result returned to LLM
6. LLM incorporates result in answer

**LLM acts as orchestrator, not executor**

---

Function Calling Overview
===

Also called:
- Function calling (OpenAI)
- Tool use (Anthropic)
- Actions (other frameworks)

**Core concept:** LLM outputs structured JSON specifying:
- Which function to call
- What parameters to pass

**System responsibility:**
- Parse the request
- Execute the function safely
- Return result to LLM

---

Example: Calculator Tool
===

**User:** "What is 1247 times 8593?"

**LLM thinks:** "I need a calculator for this"

**LLM outputs:**
```json
{
  "tool": "calculator",
  "operation": "multiply",
  "arguments": {
    "a": 1247,
    "b": 8593
  }
}
```

**System:** Executes calculator(1247, 8593) → 10,715,671

**LLM final answer:** "1247 times 8593 equals 10,715,671"

---

Tool Schema Definition
===

Tools must be defined using JSON Schema:

```json
{
  "name": "get_gene_info",
  "description": "Retrieve gene information from NCBI",
  "parameters": {
    "type": "object",
    "properties": {
      "gene_symbol": {
        "type": "string",
        "description": "Official gene symbol (e.g., 'BRCA1')"
      },
      "species": {
        "type": "string",
        "enum": ["human", "mouse", "rat"],
        "default": "human"
      }
    },
    "required": ["gene_symbol"]
  }
}
```

---

Why Schema Matters
===

**Good schema → Accurate tool selection**

The LLM uses:
- `name`: Quick identification
- `description`: When to use this tool
- `parameters.description`: What to pass

**Principle:** Write schemas for LLMs, not humans

**Bad:** "gene" (ambiguous)
**Good:** "gene_symbol: Official HUGO gene symbol"

---

Tool Schema Best Practices
===

**1. Descriptive names**
```json
{"name": "search_pubmed"}  // ✅ Clear
{"name": "search"}         // ❌ Ambiguous
```

**2. Detailed descriptions**
```json
"description": "Search PubMed database for articles matching query terms. Returns up to max_results article PMIDs."  // ✅

"description": "Searches PubMed"  // ❌ Too vague
```

**3. Constrain parameters**
```json
{"enum": ["human", "mouse"]}  // ✅ Prevents invalid input
```

---

litellm Function Calling
===

```python
from litellm import completion

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_sequence",
            "description": "Fetch DNA sequence from NCBI",
            "parameters": {
                "type": "object",
                "properties": {
                    "accession": {
                        "type": "string",
                        "description": "GenBank accession number"
                    }
                },
                "required": ["accession"]
            }
        }
    }
]

response = completion(
    model="anthropic/claude-sonnet-4-20250514",
    messages=[{"role": "user", "content": "Get sequence for NC_000001.11"}],
    tools=tools
)
```

---

Parsing Tool Calls
===

```python
response = completion(model="...", messages=[...], tools=tools)

# Check if LLM wants to use a tool
if response.choices[0].message.tool_calls:
    tool_call = response.choices[0].message.tool_calls[0]
    
    function_name = tool_call.function.name
    arguments = json.loads(tool_call.function.arguments)
    
    # Execute the function
    if function_name == "get_sequence":
        result = get_sequence(**arguments)
    
    # Return result to LLM
    messages.append({
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": str(result)
    })
    
    # Get final response
    final = completion(model="...", messages=messages, tools=tools)
```

---

NCBI E-utilities Example
===

**Implement a direct tool for gene lookup:**

```python
import requests

def get_gene_info(gene_symbol: str, species: str = "human"):
    """Get gene information from NCBI Gene database."""
    
    # Map species to taxonomy IDs
    tax_ids = {"human": "9606", "mouse": "10090"}
    
    # Search for gene
    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "gene",
        "term": f"{gene_symbol}[Gene Name] AND {tax_ids[species]}[Taxonomy ID]",
        "retmode": "json"
    }
    
    response = requests.get(search_url, params=params)
    data = response.json()
    
    if data['esearchresult']['idlist']:
        gene_id = data['esearchresult']['idlist'][0]
        # Fetch details...
        return {"gene_id": gene_id, "symbol": gene_symbol}
    
    return {"error": "Gene not found"}
```

---

Demo 1: Direct Tool Integration
===

**Live demo:** Building NCBI gene lookup tool

**Steps:**
1. Define tool schema
2. Implement Python function
3. Register with LLM
4. Test with queries
5. Handle errors

**Watch for:** How LLM decides to use tool

---

Multi-Step Tool Use
===

LLMs can chain multiple tool calls:

**User:** "Find papers about BRCA1 and summarize the most cited one"

**Step 1:** Call `search_pubmed("BRCA1")` → [PMID1, PMID2, ...]

**Step 2:** Call `get_citations(PMID1)` → 523 citations

**Step 3:** Call `get_citations(PMID2)` → 1205 citations (highest)

**Step 4:** Call `get_abstract(PMID2)` → Abstract text

**Step 5:** Generate summary based on abstract

**LLM orchestrates the sequence**

---

# Part 2: Model Context Protocol (MCP)

---

What is MCP?
===

**Model Context Protocol (MCP)** = Open standard by Anthropic

**Purpose:** Standardize how LLMs connect to:
- Data sources (files, databases, APIs)
- Tools (calculators, search, code execution)
- Services (external systems)

**Analogy:** USB for AI
- Before USB: Different cable for each device
- After USB: One standard interface
- MCP: One protocol for all LLM integrations

**Released:** Late 2024, gaining rapid adoption

---

Why MCP Matters
===

**Before MCP:**
- Every app implements tools differently
- No code reuse between projects
- Security handled inconsistently
- Each LLM needs custom integration

**With MCP:**
- Write tool once, use everywhere
- Community-shared MCP servers
- Standardized security model
- Works across LLM platforms

**Result:** Ecosystem of reusable tools

---

MCP Architecture
===

```
┌─────────────┐
│  LLM App    │  (OpenCode, Claude Desktop, etc.)
│  (Client)   │
└──────┬──────┘
       │
       │ MCP Protocol
       │ (JSON-RPC)
       │
┌──────┴──────┐
│ MCP Server  │  (Provides tools/resources)
└──────┬──────┘
       │
       ├─── Tool 1 (search files)
       ├─── Tool 2 (read database)
       └─── Tool 3 (call API)
```

**Client:** Application using LLM
**Server:** Provides tools/data
**Protocol:** Standardized communication

---

MCP Components
===

**MCP Server provides:**

1. **Resources** - Data the LLM can access
   - Files, database records, API responses

2. **Tools** - Functions the LLM can call
   - Search, compute, query, modify

3. **Prompts** - Pre-built prompt templates
   - Common tasks, workflows

**Client discovers and uses these automatically**

---

MCP vs Direct Tools
===

| Aspect | Direct Tools | MCP |
|--------|-------------|-----|
| **Reusability** | Project-specific | Reusable across apps |
| **Setup** | Write Python functions | Install MCP server |
| **Discovery** | Manual schema definition | Automatic discovery |
| **Security** | DIY | Standardized permissions |
| **Community** | Limited sharing | Growing ecosystem |
| **Flexibility** | Full control | Some constraints |

**When to use which?** (covered later)

---

MCP Servers: Examples
===

**Available MCP servers:**

**File System:**
- `@modelcontextprotocol/server-filesystem`
- Safe file access with permissions

**Databases:**
- `@modelcontextprotocol/server-postgres`
- `@modelcontextprotocol/server-sqlite`

**Development:**
- `@modelcontextprotocol/server-github`
- `@context7/mcp-server` (documentation)

**Web:**
- `@modelcontextprotocol/server-fetch`
- `@modelcontextprotocol/server-puppeteer`

**Full list:** https://github.com/modelcontextprotocol/servers

---

Context7 MCP Server
===

**Context7** = Documentation search and retrieval

**What it provides:**
- Search programming documentation
- Retrieve API references
- Get code examples
- Multi-language support

**Use case:**
"How do I use pandas.merge()?" → Context7 retrieves official docs

**We'll use this as our MCP example**

---

Installing MCP Servers
===

**MCP servers are typically Node.js packages:**

```bash
# Install an MCP server globally
npm install -g @context7/mcp-server

# Or use npx to run without installing
npx @context7/mcp-server
```

**MCP servers run as separate processes**

Client applications connect to them via:
- stdio (standard input/output)
- HTTP
- WebSocket

---

Configuring MCP in Applications
===

**Example: Claude Desktop MCP config**

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@context7/mcp-server"],
      "env": {
        "CONTEXT7_API_KEY": "your-key-here"
      }
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/workspace"]
    }
  }
}
```

**Config location:**
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%/Claude/claude_desktop_config.json`

---

Using MCP Tools
===

**Once configured, tools appear automatically:**

**User to LLM:** "Search the pandas documentation for merge examples"

**LLM sees available tools:**
```json
{
  "name": "search_docs",
  "description": "Search documentation using Context7",
  "parameters": {
    "query": "string",
    "language": "string"
  }
}
```

**LLM calls tool:**
```json
{
  "tool": "search_docs",
  "arguments": {
    "query": "pandas merge examples",
    "language": "python"
  }
}
```

**Result:** Relevant documentation returned to LLM

---

Demo 2: Using Context7 MCP Server
===

**Live demo:** Setting up and using Context7

**Steps:**
1. Install Context7 MCP server
2. Configure in Claude Desktop or compatible client
3. Query: "How do I use pandas.read_csv with custom delimiters?"
4. Observe MCP tool call
5. See documentation retrieval
6. LLM generates answer with doc references

**Key point:** No Python code written by us!

---

MCP Security Model
===

**MCP provides built-in security:**

**1. Explicit permissions**
```json
"filesystem": {
  "command": "...",
  "allowedPaths": ["/safe/directory"],
  "readOnly": true
}
```

**2. Capability-based access**
- Server declares what it can do
- Client approves capabilities
- User controls scope

**3. Sandboxing**
- MCP servers run as separate processes
- Limited system access
- Can't access arbitrary files

**4. Audit trail**
- All tool calls logged
- Traceable actions

---

MCP Discovery Process
===

**How client learns about tools:**

```
1. Client starts MCP server
   ↓
2. Client: "initialize" request
   ↓
3. Server responds with capabilities:
   {
     "tools": [
       {"name": "search_docs", ...},
       {"name": "get_example", ...}
     ],
     "resources": [...],
     "prompts": [...]
   }
   ↓
4. Client now knows all available tools
   ↓
5. LLM can call tools as needed
```

**No manual schema writing!**

---

MCP Protocol Deep Dive
===

**MCP uses JSON-RPC 2.0:**

**Tool call request:**
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "search_docs",
    "arguments": {
      "query": "pandas merge"
    }
  }
}
```

**Tool call response:**
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "pandas.merge() documentation..."
      }
    ]
  }
}
```

---

Building Custom MCP Servers
===

**Advanced topic** (not covered today, but preview):

```typescript
// TypeScript MCP Server skeleton
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new Server({
  name: "my-bioinformatics-server",
  version: "1.0.0"
});

// Register a tool
server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [{
    name: "query_gene_database",
    description: "Query gene information",
    inputSchema: { /* JSON Schema */ }
  }]
}));

// Handle tool execution
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "query_gene_database") {
    // Execute tool logic
    return { result: data };
  }
});
```

**For future sessions or advanced students**

---

# Part 3: Comparison & Best Practices

---

When to Use Direct Tools
===

**Choose direct tools when:**

✅ **One-off integration** - Won't reuse elsewhere

✅ **Simple function** - Just a few lines of Python

✅ **Full control needed** - Custom error handling, caching

✅ **No suitable MCP server** - Tool doesn't exist yet

✅ **Learning** - Understanding tool mechanics

✅ **Prototype** - Quick testing

**Example:** Custom lab equipment API

---

When to Use MCP
===

**Choose MCP when:**

✅ **Reusability** - Multiple projects will use it

✅ **Security matters** - Need controlled access

✅ **Community tools** - Existing MCP server available

✅ **Standard operations** - File access, DB queries, web search

✅ **Multiple LLM apps** - Want consistent interface

✅ **Team collaboration** - Shared tool infrastructure

**Example:** Documentation search, file system access

---

Hybrid Approach
===

**Best practice:** Use both!

```python
# MCP for standard operations
- File system access (MCP filesystem server)
- Documentation search (Context7 MCP)
- Database queries (MCP postgres server)

# Direct tools for custom needs
- Lab-specific API integrations
- Custom bioinformatics algorithms
- Proprietary database access
- One-off calculations
```

**MCP for infrastructure, direct tools for specialization**

---

Error Handling: Direct Tools
===

```python
def get_gene_info(gene_symbol: str):
    try:
        result = query_ncbi(gene_symbol)
        return {"success": True, "data": result}
    except requests.RequestException as e:
        return {
            "success": False,
            "error": f"Network error: {str(e)}",
            "retry": True
        }
    except KeyError:
        return {
            "success": False,
            "error": "Gene not found",
            "retry": False
        }
```

**Return structured errors to LLM**

---

Error Handling: MCP
===

**MCP has standardized error responses:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": -32603,
    "message": "Internal error",
    "data": {
      "details": "Network timeout"
    }
  }
}
```

**Error codes:**
- `-32700`: Parse error
- `-32600`: Invalid request
- `-32601`: Method not found
- `-32603`: Internal error

**LLM can interpret and retry appropriately**

---

Security Considerations
===

**Direct tools:**
- ⚠️ Validate all parameters
- ⚠️ Sanitize inputs (SQL injection, path traversal)
- ⚠️ Rate limiting
- ⚠️ Credential management
- ⚠️ Audit logging

**MCP:**
- ✅ Built-in permission system
- ✅ Sandboxed execution
- ✅ Explicit capability grants
- ✅ Standardized security model
- ⚠️ Still validate MCP server trustworthiness

**Defense in depth:** Security at all layers

---

Tool Performance
===

**Direct tools:**
- Fast (no protocol overhead)
- Can optimize freely
- In-process execution

**MCP:**
- Small protocol overhead (JSON-RPC)
- Separate process (inter-process communication)
- Worth it for security/reusability

**Benchmark:** MCP adds ~10-50ms per tool call
**Usually negligible compared to LLM latency**

---

The MCP Ecosystem
===

**Growing rapidly:**

**Official servers:** 20+ from Anthropic
**Community servers:** 100+ and counting
**Platforms integrating MCP:**
- Claude Desktop
- OpenCode
- Cline
- Zed Editor
- Continue.dev

**Future:** Expected to become standard

**Get involved:** https://github.com/modelcontextprotocol

---

Practical Demo Summary
===

**What we demonstrated:**

✅ **Direct tools:**
- Wrote Python function for NCBI
- Defined JSON schema
- Integrated with litellm
- Handled errors

✅ **MCP:**
- Installed Context7 server
- Configured in client
- Used documentation search
- Zero Python code for the tool

**Key insight:** Both approaches valid, choose by needs

---

Multi-Step with MCP
===

**MCP tools can be chained:**

**User:** "Find Python documentation for file I/O, then show me an example from our codebase"

**Step 1 (MCP):** Context7 searches Python docs
**Step 2 (MCP):** Filesystem server searches local files
**Step 3 (LLM):** Synthesizes example

**MCP servers can be composed naturally**

---

OpenCode & MCP Preview
===

**Looking ahead to Session 5:**

**OpenCode integrates with MCP servers:**
- Can use Context7 for documentation
- Can use filesystem server for code access
- Can use custom MCP servers you build
- All configured in OpenCode settings

**Session 5 will show:**
- Configuring MCP servers in OpenCode
- Using Context7 during development
- How MCP enhances AI-assisted coding

**MCP is becoming infrastructure for AI coding**

---

Key Takeaways
===

1. **Two approaches:** Direct tools (Python functions) vs MCP (standardized servers)

2. **Direct tools:** Full control, quick prototyping, custom needs

3. **MCP:** Reusability, security, community ecosystem

4. **MCP architecture:** Client-server with JSON-RPC protocol

5. **Use both:** MCP for infrastructure, direct for specialization

6. **Context7 example:** Documentation search without custom code

7. **Security:** MCP provides standardized permissions

8. **Growing ecosystem:** Many servers available, more coming

---

Theory ↔ Practice Connections
===

**Theory:** LLMs trained on API documentation and function signatures

**Practice:** Both direct tools and MCP leverage this training

---

**Theory:** Context window limitations require external data access

**Practice:** Tools (direct or MCP) fetch data dynamically

---

**Theory:** Standardization reduces cognitive load

**Practice:** MCP's standard protocol simplifies integration

---

Resources
===

**MCP:**
- Official site: https://modelcontextprotocol.io/
- GitHub: https://github.com/modelcontextprotocol
- Server list: https://github.com/modelcontextprotocol/servers
- Spec: https://spec.modelcontextprotocol.io/

**Context7:**
- MCP Server: https://github.com/context7/mcp-server

**Direct tool integration:**
- NCBI E-utilities: https://www.ncbi.nlm.nih.gov/books/NBK25501/
- OpenAI Function Calling: https://platform.openai.com/docs/guides/function-calling
- Anthropic Tool Use: https://docs.anthropic.com/claude/docs/tool-use

**Demo code:** `lectures/demos/session_4/`

---

Looking Ahead: Session 5
===

**Next topic:** AI Agents

**The evolution:**

**Session 0:** Foundation - LLM fundamentals

**Session 1:** Interface - Coding with LLMs

**Session 2:** Advanced prompting for single interactions

**Session 3:** RAG for knowledge retrieval

**Session 4:** Tools (direct + MCP) for dynamic actions

**Session 5:** Agents that autonomously loop: Perceive → Reason → Act
- Agents can use both direct tools AND MCP servers
- Multi-step autonomous workflows
- Self-directed tool selection

---

Questions?
===

**Next session:** AI Agents - Autonomous Reasoning Systems

**Optional homework:**
- Install Context7 MCP server
- Try Claude Desktop with MCP
- Explore available MCP servers
- Think about custom tools you might need
