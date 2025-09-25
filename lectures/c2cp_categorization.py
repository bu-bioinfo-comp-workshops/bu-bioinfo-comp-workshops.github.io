from litellm import completion
import os
import dotenv
import random

dotenv.load_dotenv()

import json

with open('c2.cp.v2025.1.Hs.json') as f:
    c2cp = json.load(f)

print(f"{len(c2cp)} gene sets in the database")

system_prompt = {
        "content": ("You are an expect at molecular biology and genetics. "
                    "You can examine lists of genes and other basic gene set "
                    "information and categorize genes into high level categories "
                    "based on the genes function."
                    ),
        "role": "system"
}

user_prompt = """
Consider the following MSigDB gene set information:

Gene set name: {gset_name}

{gset}

Attempt to label the gene set into one of the following categories:

- Inflammation
- Cell cycle
- Immune System
- Cytoskeleton
- Development
- Metabolism
- Transcription/Translation
- Other

The 'Other' category should include gene sets that don't fit well into
any of the other categories.

Respond with valid JSON output of the form:

{{
    "category": "your label",
    "rationale": "brief explanation of why you made the choice"
}}

Make sure to provide a rationale based on the content of the gene set
description.
"""

gsets = random.sample(list(c2cp.items()), 10)

for k, gset in gsets:

    gset_prompt = user_prompt.format(
            gset_name=k,
            gset=json.dumps(gset)
    )

    response = completion(
      model="anthropic/claude-4-sonnet-20250514",
      messages=[
          system_prompt,
          {"content": gset_prompt, "role": "user"}
      ]
    )

    resp_json = response['choices'][0]['message']['content']
    try:
        response = json.loads(resp_json)
        category = response.get('category')
        rationale = response.get('rationale')
        print(f"{category}: {k}, {rationale}")
    except:
        print("JSON malform")
        print(resp_json)
