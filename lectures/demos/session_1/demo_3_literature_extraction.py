"""
Demo 3: Literature Data Extraction with Chain-of-Thought

This demo extracts structured data from PubMed abstracts using
chain-of-thought prompting combined with JSON schema enforcement.
"""

from litellm import completion
import dotenv
import json

dotenv.load_dotenv()

print("=" * 80)
print("Demo 3: Literature Data Extraction - Chain of Thought + JSON")
print("=" * 80)

# Sample PubMed abstract
ABSTRACT = """
Mutations in the BRCA1 gene are associated with increased risk of breast and 
ovarian cancer. We performed whole-exome sequencing on 500 patients with 
familial breast cancer and identified 23 novel pathogenic variants. The study 
population consisted of women aged 25-65 (mean age 42) recruited from oncology 
clinics across North America between 2018-2020. The most common variant, 
c.5266dupC, was found in 8% of cases. All patients provided informed consent, 
and the study was approved by the institutional review board. Our findings 
suggest that genetic testing should be expanded to include younger women with 
family history.
"""

# ============================================================================
# Version 1: Direct Extraction (No CoT)
# ============================================================================
print("\n--- Version 1: Direct Extraction (No Chain-of-Thought) ---\n")

direct_prompt = f"""
Extract the following information from this abstract and return as JSON:

{{
  "gene": "gene name if mentioned",
  "disease": "primary disease studied",
  "sample_size": "number of participants",
  "age_range": "age range of participants",
  "key_finding": "main result",
  "study_period": "years of data collection"
}}

Abstract:
{ABSTRACT}
"""

response = completion(
    model="anthropic/claude-sonnet-4-20250514",
    messages=[{"role": "user", "content": direct_prompt}],
)

print("Response:")
response_text = response["choices"][0]["message"]["content"]
print(response_text)

# Try to parse
try:
    if "```json" in response_text:
        response_text = response_text.split("```json")[1].split("```")[0].strip()
    elif "```" in response_text:
        response_text = response_text.split("```")[1].split("```")[0].strip()

    parsed = json.loads(response_text)
    print("\n✅ Parsed successfully")
    print(json.dumps(parsed, indent=2))
except json.JSONDecodeError as e:
    print(f"\n❌ Parsing failed: {e}")

print("\n💭 This works, but might miss nuances or make extraction errors")
print("   for complex abstracts with multiple findings.")

input("\n[Press Enter for Chain-of-Thought version...]")

# ============================================================================
# Version 2: Chain-of-Thought Extraction
# ============================================================================
print("\n--- Version 2: Chain-of-Thought Extraction ---\n")

cot_prompt = f"""
Extract structured data from this biomedical abstract. Let's work through this step by step:

1. First, identify the main gene or genes mentioned
2. Then, identify the disease or condition being studied
3. Find sample size information (number of participants)
4. Look for demographic information (age, gender, etc.)
5. Identify the key finding or conclusion
6. Note the study period if mentioned
7. Check for any additional relevant details (variants, percentages, etc.)

After analyzing, provide the extracted information in this JSON format:

{{
  "gene": "gene name(s)",
  "disease": "disease or condition",
  "sample_size": number,
  "demographics": {{
    "age_range": "range",
    "mean_age": number or null,
    "gender": "if specified"
  }},
  "study_period": "years",
  "key_findings": [
    "finding 1",
    "finding 2"
  ],
  "notable_variants": [
    {{
      "variant": "variant notation",
      "frequency": "percentage if given"
    }}
  ]
}}

Abstract:
{ABSTRACT}

Let's think through this step by step:
"""

response = completion(
    model="anthropic/claude-sonnet-4-20250514",
    messages=[{"role": "user", "content": cot_prompt}],
)

print("Response (with reasoning):")
response_text = response["choices"][0]["message"]["content"]
print(response_text)

# Extract JSON from response
print("\n" + "=" * 80)
print("Attempting to parse final JSON...")
print("=" * 80)

try:
    # The response might contain reasoning text before the JSON
    if "```json" in response_text:
        json_text = response_text.split("```json")[1].split("```")[0].strip()
    elif "```" in response_text:
        json_text = response_text.split("```")[1].split("```")[0].strip()
    else:
        # Try to find JSON object in text
        import re

        json_match = re.search(r"\{[\s\S]*\}", response_text)
        if json_match:
            json_text = json_match.group()
        else:
            json_text = response_text

    parsed = json.loads(json_text)
    print("\n✅ Parsed successfully!")
    print("\nExtracted structured data:")
    print(json.dumps(parsed, indent=2))

except json.JSONDecodeError as e:
    print(f"\n❌ Parsing failed: {e}")
    print("Raw JSON attempt:")
    print(json_text if "json_text" in locals() else response_text)

print("\n✅ ADVANTAGES of Chain-of-Thought:")
print("  - More thorough extraction")
print("  - Better handling of complex information")
print("  - Explicit reasoning visible")
print("  - Less likely to miss important details")
print("  - Can trace errors in reasoning")

input("\n[Press Enter for comparison with multiple abstracts...]")

# ============================================================================
# Comparison: Multiple Abstracts
# ============================================================================
print("\n--- Processing Multiple Abstracts ---\n")

abstracts = [
    {
        "title": "TP53 mutations in lung cancer",
        "text": """
        Analysis of TP53 mutations in 200 lung adenocarcinoma patients revealed
        that 65% carried at least one pathogenic variant. Patients ranged from
        45-80 years old. The R273H missense mutation was most common (15% of cases).
        Study conducted 2019-2021 in European hospitals.
        """,
    },
    {
        "title": "CFTR gene therapy trial",
        "text": """
        A phase 2 clinical trial of CFTR gene therapy in cystic fibrosis included
        30 pediatric patients (ages 6-12). The trial ran from January 2020 to
        December 2022. Treatment resulted in 40% improvement in lung function
        scores. The most common CFTR variant in the cohort was F508del (70% of
        patients).
        """,
    },
]

# Using CoT approach for batch processing
batch_prompt = """
Extract data from these biomedical abstracts. For each, think step-by-step
to identify: gene, disease, sample size, age range, study period, and key findings.

Return as a JSON array where each element has this structure:
{
  "title": "study focus",
  "gene": "gene name",
  "disease": "condition",
  "sample_size": number,
  "age_range": "range",
  "study_period": "years",
  "key_variant": {"name": "...", "frequency": "..."},
  "main_finding": "..."
}

Abstracts:
"""

for i, abstract in enumerate(abstracts, 1):
    batch_prompt += f"\n\nAbstract {i}: {abstract['title']}\n{abstract['text']}"

response = completion(
    model="anthropic/claude-sonnet-4-20250514",
    messages=[{"role": "user", "content": batch_prompt}],
)

print("Batch extraction results:")
response_text = response["choices"][0]["message"]["content"]
print(response_text)

# Parse the array
try:
    if "```json" in response_text:
        json_text = response_text.split("```json")[1].split("```")[0].strip()
    elif "```" in response_text:
        json_text = response_text.split("```")[1].split("```")[0].strip()
    else:
        import re

        json_match = re.search(r"\[[\s\S]*\]", response_text)
        if json_match:
            json_text = json_match.group()
        else:
            json_text = response_text

    parsed = json.loads(json_text)
    print("\n✅ Batch parsing successful!")
    print("\nExtracted from", len(parsed), "abstracts:")
    for i, item in enumerate(parsed, 1):
        print(f"\nAbstract {i}:")
        print(json.dumps(item, indent=2))

except json.JSONDecodeError as e:
    print(f"\n❌ Parsing failed: {e}")

print("\n" + "=" * 80)
print("Summary: Literature Extraction Best Practices")
print("=" * 80)
print("✅ Use chain-of-thought for complex extractions")
print("✅ Specify exact JSON schema expected")
print("✅ Process similar items in batches (more efficient)")
print("✅ Make reasoning explicit ('step by step')")
print("✅ Handle missing fields gracefully (null values)")
print("\n💡 Real-world application: Automated systematic reviews")
print("=" * 80)
