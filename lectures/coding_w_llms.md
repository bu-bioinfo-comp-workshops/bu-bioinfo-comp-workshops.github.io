---
title: Coding with LLMs
options:
    end_slide_shorthand: true
---

Coding with LLMs
===

- LLMs are only matrices

- We need tools that interface with them

---

<!-- jump_to_middle -->

Chatbots like ChatGPT are designed around human conversations

They were the first "killer apps" for LLMs

---

<!-- jump_to_middle -->

Chatbots interact with LLMs *programmatically* by sending inputs and receiving outputs
===

---

<!-- jump_to_middle -->

We can do the same thing in our code and environments

iow, we can "cut out the middle man" chatbot and use LLMs directly

---

LLM Development Workflow
===

1. Identify LLM provider that provides an API
2. Generate API key
3. Choose LLM library/tools
4. Send LLM input, integrate output

---

<!-- jump_to_middle -->

Part 1: Identify LLM provider
===

---

LLM Providers and APIs
===

- **Application Programming Interface**
- Allows code to make calls to remote services
- Most mainstream LLM providers have API access to their models, e.g.
    - OpenAI
    - Anthropic
    - Meta Llama
    - Google Gemini
    - Amazon Nova
    - Model routing services like [openrouter.ai](https://openrouter.ai)

---

Standard API characteristics
===

- APIs expose *endpoints* that accept JSON formatted requests
- Endpoints are URLs, e.g. `https://api.anthropic.com/v1/models`

```bash
curl https://api.anthropic.com/v1/models \ 
    -H "Content-Type: application/json" \
    -H "x-api-key: $(llm keys get anthropic)" \
    -H "anthropic-version: 2023-06-01"  | jq
```

---

```json
{
  "data": [
    {
      "type": "model",
      "id": "claude-opus-4-1-20250805",
      "display_name": "Claude Opus 4.1",
      "created_at": "2025-08-05T00:00:00Z"
    },
    {
      "type": "model",
      "id": "claude-opus-4-20250514",
      "display_name": "Claude Opus 4",
      "created_at": "2025-05-22T00:00:00Z"
    }
  ]
}
```

---

APIs accept and return JSON formatted text
===

```json
{
    "messages": [
        {
            "content": "Hello, how are you?",
            "role": "user"
        }
    ]
}
```

The structure of the input and responses is now (mostly) standardized across providers

---

API endpoints defined in provider docs
===

- There are often many different endpoints:
    - `/models`
    - `/complete`
    - `/messages` etc...
- Documented in the developer documentation, e.g. _https://docs.claude.com/en/docs/_
- Unless we're developing a sophisticated application, usually don't need to know about these endpoints...

---

<!-- jump_to_middle -->

Part 2: Generate API Key
===

---

Most APIs require a key to authenticate
===

- An API *key* (or *token*) must be sent along with requests
- A key is simply a long sequence of characters
    - e.g. `sk-ant-IjcOVgUYbqqdoLPP3UAbGRyODx...`
- We create these keys using tools provided by the LLM providers
- **Keys are like passwords! Keep them secret!**

```bash
curl https://api.anthropic.com/v1/models \
    -H "Content-Type: application/json" \
    -H "x-api-key: sk-ant-IjcOV..." \ # <- API key
    -H "anthropic-version: 2023-06-01"  | jq
```

---

<!-- jump_to_middle -->

Super secure API key generation demo
===

---

`.env` secrets file convention
===

- A current convention is to keep secret values used by software projects in a file named `.env`
- Format `KEY=VALUE`
- e.g.

```
ANTHROPIC_KEY=sk-ant-IjcOVgUYbqqdoLPP3UAbGRyODx
OPENAI_KEY=sk-proj-1234567890abcdef1234567890ab
```

- Don't check into git repos, add to `.gitignore`!

---

`.env` secrets file convention cont'd
===

- In bash, can load in secrets from `.env` to your environment with:

```bash
echo ANTHROPIC_API_KEY=sk-ant-IjcoV... >> .env
set -a
source .env
set +a

curl https://api.anthropic.com/v1/models \
    -H "Content-Type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"  | jq
```

---

<!-- jump_to_middle -->

Choose LLM library
===

---

Software libraries wrap API calls
===

- We can call these API endpoints from our code
- Most popular languages have libraries that make this easy
- Need to specify an API key, like on the command line

---

LLMs in python
===

- In `python` we can use [litellm](https://docs.litellm.ai/docs/)

```python
from litellm import completion
import os

## ANTHROPIC_API_KEY must be set in environment
response = completion(
  model="anthropic/claude-4-sonnet-20250514",
  messages=[{
    "content": "Hello, how are you?",
    "role": "user"
  }]
)
print(response.json())
```

---

Response

```python
{"choices": [{"finish_reason": "stop",
      "index": 0,
      "message": {"content": "Hello! I'm doing well, thank you for "
                             "asking. I'm here and ready to help with "
                             "whatever you'd like to discuss or work "
                             "on. How are you doing today?",
                  "function_call": None,
                  "role": "assistant",
                  "tool_calls": None}}],
 "created": 1758822587,
 "id": "chatcmpl-e02204e5-5c20-47dd-b6c5-f8f1c8f7a5ba",
 "model": "claude-sonnet-4-20250514",
 "object": "chat.completion",
 ...
```

---

```python
...
 "system_fingerprint": None,
 "usage": {"cache_creation_input_tokens": 0,
           "cache_read_input_tokens": 0,
           "completion_tokens": 39,
           "completion_tokens_details": None,
           "prompt_tokens": 13,
           "prompt_tokens_details": {"audio_tokens": None,
                 "cache_creation_token_details": {
                     "ephemeral_1h_input_tokens": 0,
                      "ephemeral_5m_input_tokens": 0
                  },
                 "cache_creation_tokens": 0,
                 "cached_tokens": 0,
                 "image_tokens": None,
                 "text_tokens": None},
           "total_tokens": 52 } }
```

---

Workshop setup
===

- Create new python virtual environment:
    - `python -m venv .venv`
- Activate environment
    - `source .venv/bin/activate`
- Install litellm:
    - `pip install litellm`
- Set `ANTHROPIC_API_KEY` in `.env`
    - `echo ANTHROPIC_API_KEY=sk-ant-XXX > .env`
    - `set -a; source .env; set +a`
- Run python litellm demo
    - `python litellm_demo.py`

