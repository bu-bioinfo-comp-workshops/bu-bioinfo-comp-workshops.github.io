"""
Demo 1: Gene Function Annotation - Evolution of a Prompt

This demo shows the iterative improvement of prompts for gene annotation.
We'll go from a naive prompt to a sophisticated structured output with examples.
"""

from litellm import completion
import dotenv
import json

dotenv.load_dotenv()

# Test gene
GENE_SYMBOL = "BRCA1"

print("=" * 80)
print("Demo 1: Gene Function Annotation - Prompt Evolution")
print("=" * 80)

# ============================================================================
# Version 1: Naive Prompt
# ============================================================================
print("\n--- Version 1: Naive Prompt ---\n")

v1_messages = [
    {"role": "user", "content": f"What does the {GENE_SYMBOL} gene do?"}
]

response = completion(
    model="anthropic/claude-sonnet-4-20250514",
    messages=v1_messages
)

print("PROMPT:")
print(v1_messages[0]["content"])
print("\nRESPONSE:")
print(response['choices'][0]['message']['content'])

print("\n💡 ISSUES:")
print("- Unstructured output (hard to parse)")
print("- Variable format (inconsistent across queries)")
print("- May include unnecessary details")

input("\n[Press Enter to continue to Version 2...]")

# ============================================================================
# Version 2: With System Prompt
# ============================================================================
print("\n--- Version 2: With System Prompt ---\n")

v2_messages = [
    {
        "role": "system",
        "content": (
            "You are a molecular biology expert specializing in human genetics. "
            "Provide concise, accurate gene annotations suitable for researchers. "
            "Focus on primary function, disease associations, and cellular location."
        )
    },
    {
        "role": "user",
        "content": f"Annotate the {GENE_SYMBOL} gene."
    }
]

response = completion(
    model="anthropic/claude-sonnet-4-20250514",
    messages=v2_messages
)

print("SYSTEM PROMPT:")
print(v2_messages[0]["content"])
print("\nUSER PROMPT:")
print(v2_messages[1]["content"])
print("\nRESPONSE:")
print(response['choices'][0]['message']['content'])

print("\n✅ IMPROVEMENTS:")
print("- More focused on relevant information")
print("- Consistent expertise level")
print("- Better suited for research context")

print("\n❌ STILL ISSUES:")
print("- Output format still varies")
print("- Not machine-parseable")

input("\n[Press Enter to continue to Version 3...]")

# ============================================================================
# Version 3: Structured JSON Output
# ============================================================================
print("\n--- Version 3: Structured JSON Output ---\n")

v3_messages = [
    {
        "role": "system",
        "content": (
            "You are a molecular biology expert specializing in human genetics. "
            "Provide gene annotations in strict JSON format. "
            "Always include: symbol, name, function, location, diseases."
        )
    },
    {
        "role": "user",
        "content": f"""
Annotate the {GENE_SYMBOL} gene. Return ONLY valid JSON in this format:

{{
  "symbol": "gene symbol",
  "name": "full gene name",
  "function": "primary molecular function",
  "location": "chromosomal location",
  "diseases": ["disease 1", "disease 2"],
  "pathway": "primary pathway involvement"
}}
"""
    }
]

response = completion(
    model="anthropic/claude-sonnet-4-20250514",
    messages=v3_messages
)

print("USER PROMPT:")
print(v3_messages[1]["content"])
print("\nRESPONSE:")
response_text = response['choices'][0]['message']['content']
print(response_text)

# Try to parse the JSON
try:
    # Remove potential markdown code fences
    if "```json" in response_text:
        response_text = response_text.split("```json")[1].split("```")[0].strip()
    elif "```" in response_text:
        response_text = response_text.split("```")[1].split("```")[0].strip()
    
    parsed_json = json.loads(response_text)
    print("\n✅ JSON PARSED SUCCESSFULLY!")
    print("\nParsed data:")
    for key, value in parsed_json.items():
        print(f"  {key}: {value}")
except json.JSONDecodeError as e:
    print(f"\n❌ JSON parsing failed: {e}")

print("\n✅ IMPROVEMENTS:")
print("- Structured, consistent format")
print("- Machine-parseable")
print("- Predictable schema")

input("\n[Press Enter to continue to Version 4...]")

# ============================================================================
# Version 4: Few-Shot Learning with Multiple Examples
# ============================================================================
print("\n--- Version 4: Few-Shot Learning ---\n")

v4_messages = [
    {
        "role": "system",
        "content": (
            "You are a molecular biology expert. Provide gene annotations "
            "in JSON format following the examples shown."
        )
    },
    {
        "role": "user",
        "content": """
I'll show you examples of gene annotations, then you'll annotate a new gene.

Example 1:
Gene: TP53
{
  "symbol": "TP53",
  "name": "tumor protein p53",
  "function": "transcription factor regulating cell cycle and apoptosis",
  "location": "17p13.1",
  "diseases": ["Li-Fraumeni syndrome", "various cancers"],
  "pathway": "p53 signaling pathway"
}

Example 2:
Gene: CFTR
{
  "symbol": "CFTR",
  "name": "cystic fibrosis transmembrane conductance regulator",
  "function": "chloride channel involved in ion transport",
  "location": "7q31.2",
  "diseases": ["cystic fibrosis", "congenital bilateral absence of vas deferens"],
  "pathway": "ABC transporter pathway"
}

Now annotate this gene:
Gene: BRCA1
"""
    }
]

response = completion(
    model="anthropic/claude-sonnet-4-20250514",
    messages=v4_messages
)

print("USER PROMPT (with examples):")
print(v4_messages[1]["content"])
print("\nRESPONSE:")
response_text = response['choices'][0]['message']['content']
print(response_text)

# Parse JSON
try:
    if "```json" in response_text:
        response_text = response_text.split("```json")[1].split("```")[0].strip()
    elif "```" in response_text:
        response_text = response_text.split("```")[1].split("```")[0].strip()
    
    parsed_json = json.loads(response_text)
    print("\n✅ JSON PARSED SUCCESSFULLY!")
    print("\nParsed data:")
    print(json.dumps(parsed_json, indent=2))
except json.JSONDecodeError as e:
    print(f"\n❌ JSON parsing failed: {e}")

print("\n✅ FINAL IMPROVEMENTS:")
print("- Consistent format learned from examples")
print("- More reliable JSON structure")
print("- Better field content quality")
print("- Shows the model the desired style/detail level")

print("\n" + "=" * 80)
print("Summary: The Evolution")
print("=" * 80)
print("V1: Naive → unstructured, variable")
print("V2: System prompt → focused, but still unstructured")
print("V3: JSON request → structured, but may vary")
print("V4: Few-shot → consistent, accurate, structured")
print("\n💡 Key lesson: Examples > Descriptions")
print("=" * 80)
