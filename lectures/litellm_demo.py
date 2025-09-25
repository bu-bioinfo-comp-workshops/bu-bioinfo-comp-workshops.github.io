from litellm import completion
import os
import dotenv

dotenv.load_dotenv()

response = completion(
  model="anthropic/claude-4-sonnet-20250514",
  messages=[{ "content": "Hello, how are you?","role": "user"}]
)

from pprint import pprint
pprint(response.json())
