import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

content_string = sys.argv[1]

messages = [
    types.Content(role="user", parts = [types.Part(text = content_string)])
]

if len(content_string) < 1:
    print("No prompt provided")
    sys.exit(1)

response = client.models.generate_content(model = "gemini-2.0-flash-001", contents=messages)

verbose = len(sys.argv) > 2 and sys.argv[2] == "--verbose"

if verbose:
    print(f"User prompt: {content_string}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

print(response.text)