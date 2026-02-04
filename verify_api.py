import llm_client
import sys

print("Testing API connection...")
response = llm_client.query_gemini("Hello, are you ready?", [{"type": "function", "function": {"name": "test", "description": "test"}}])

if "error" in response:
    with open("error.log", "w") as f:
        f.write(str(response))
    print(f"FAILED: See error.log")
    sys.exit(1)
else:
    print("SUCCESS: Connection established.")
    print(response)
    sys.exit(0)
