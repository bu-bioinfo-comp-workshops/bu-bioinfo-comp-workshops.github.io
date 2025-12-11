"""
Demo 2: Sequence Motif Classification with Few-Shot Learning

This demo shows how few-shot learning helps classify DNA regulatory motifs
by their function, using biological examples to train the model in-context.
"""

from litellm import completion
import dotenv
import json

dotenv.load_dotenv()

print("=" * 80)
print("Demo 2: DNA Motif Classification - Few-Shot Learning")
print("=" * 80)

# Test motifs to classify
test_motifs = [
    ("TATAAA", "Unknown regulatory element"),
    ("CCAAT", "Unknown regulatory element"),
    ("GGGCGG", "Unknown regulatory element"),
    ("AATAAA", "Unknown regulatory element"),
]

# ============================================================================
# Version 1: Zero-Shot (No Examples)
# ============================================================================
print("\n--- Version 1: Zero-Shot Classification ---\n")

system_prompt = {
    "role": "system",
    "content": (
        "You are an expert in gene regulation and promoter elements. "
        "Classify DNA sequence motifs by their regulatory function."
    ),
}

for motif, description in test_motifs[:2]:  # Just test first 2
    user_prompt = {
        "role": "user",
        "content": f"""
Classify this DNA motif by its regulatory function.

Motif: {motif}

Provide classification in JSON format:
{{
  "motif": "sequence",
  "function": "regulatory function",
  "location": "typical genomic location",
  "binding_factors": ["factor1", "factor2"]
}}
""",
    }

    response = completion(
        model="anthropic/claude-sonnet-4-20250514",
        messages=[system_prompt, user_prompt],
    )

    print(f"Motif: {motif}")
    print("Response:")
    print(response["choices"][0]["message"]["content"])
    print()

print("❌ ISSUES with zero-shot:")
print("- May miss specific biological context")
print("- Classifications might be too general")
print("- Format might vary despite JSON request")

input("\n[Press Enter to continue to Few-Shot version...]")

# ============================================================================
# Version 2: Few-Shot with Biological Examples
# ============================================================================
print("\n--- Version 2: Few-Shot with Examples ---\n")

few_shot_prompt = {
    "role": "user",
    "content": """
I'll show you examples of DNA regulatory motif classifications, then you classify new motifs.

Example 1:
Motif: CAAT
{
  "motif": "CAAT",
  "function": "CAAT box - transcription factor binding site",
  "location": "typically -75 to -80 bp upstream of TSS",
  "binding_factors": ["NF-Y", "CTF", "C/EBP"],
  "effect": "enhances transcription initiation"
}

Example 2:
Motif: CACGTG
{
  "motif": "CACGTG",
  "function": "E-box - basic helix-loop-helix transcription factor binding",
  "location": "enhancers and promoters, variable distance from TSS",
  "binding_factors": ["MYC", "MAX", "USF"],
  "effect": "regulates cell cycle and differentiation genes"
}

Example 3:
Motif: GGGCGG
{
  "motif": "GGGCGG",
  "function": "GC box - Sp1 transcription factor binding site",
  "location": "-40 to -110 bp upstream of TSS, common in TATA-less promoters",
  "binding_factors": ["Sp1", "Sp3", "KLF family"],
  "effect": "maintains basal transcription in housekeeping genes"
}

Now classify these new motifs:

Motif 1: TATAAA
Motif 2: CCAAT
Motif 3: AATAAA
Motif 4: GGGCGG

For each motif, provide the same JSON format as shown in examples.
""",
}

response = completion(
    model="anthropic/claude-sonnet-4-20250514",
    messages=[system_prompt, few_shot_prompt],
)

print("RESPONSE:")
print(response["choices"][0]["message"]["content"])

print("\n✅ IMPROVEMENTS with few-shot:")
print("- More specific biological terminology")
print("- Consistent level of detail")
print("- Accurate functional classifications")
print("- Proper binding factor identification")
print("- Consistent JSON structure")

input("\n[Press Enter to see comparison...]")

# ============================================================================
# Comparison: Zero-Shot vs Few-Shot on Same Motif
# ============================================================================
print("\n--- Direct Comparison on TATAAA Motif ---\n")

# Zero-shot
print("ZERO-SHOT APPROACH:")
zero_shot_msg = {
    "role": "user",
    "content": "Classify the TATAAA DNA motif. Return JSON with: motif, function, location, binding_factors.",
}

response_zero = completion(
    model="anthropic/claude-sonnet-4-20250514", messages=[system_prompt, zero_shot_msg]
)

print(response_zero["choices"][0]["message"]["content"])

print("\n" + "-" * 80 + "\n")

# Few-shot
print("FEW-SHOT APPROACH (with context):")

few_shot_single = {
    "role": "user",
    "content": """
Example classifications:

Motif: CCAAT
{
  "motif": "CCAAT",
  "function": "CCAAT box - enhancer element",
  "location": "-60 to -100 bp from TSS",
  "binding_factors": ["NF-Y", "CTF"],
  "effect": "increases transcription rate"
}

Motif: GGGCGG
{
  "motif": "GGGCGG", 
  "function": "GC box - Sp1 binding site",
  "location": "proximal promoter, TATA-less promoters",
  "binding_factors": ["Sp1", "Sp3"],
  "effect": "basal transcription in housekeeping genes"
}

Now classify:
Motif: TATAAA
""",
}

response_few = completion(
    model="anthropic/claude-sonnet-4-20250514",
    messages=[system_prompt, few_shot_single],
)

print(response_few["choices"][0]["message"]["content"])

print("\n" + "=" * 80)
print("Summary: Few-Shot Learning Impact")
print("=" * 80)
print("✅ Few-shot provides:")
print("  - Consistent format and detail level")
print("  - Domain-appropriate terminology")
print("  - Expected information granularity")
print("  - Pattern matching from examples")
print("\n💡 Key insight: Examples teach the model your specific needs")
print("   better than lengthy instructions ever could")
print("=" * 80)
