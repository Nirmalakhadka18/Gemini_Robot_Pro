import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "google/gemini-pro-1.5")
SITE_URL = "https://github.com/Antigravity" # Optional OpenRouter headers
SITE_NAME = "GeminiRobotCLI"

def query_gemini(user_prompt: str, tools_schema: list = None):
    """
    Sends a prompt to OpenRouter (Gemini) with optional tools.
    """
    if not OPENROUTER_API_KEY:
        raise ValueError("OPENROUTER_API_KEY not found in environment variables.")

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": SITE_URL,
        "X-Title": SITE_NAME,
        "Content-Type": "application/json"
    }

    messages = [
        {"role": "system", "content": "You are a helpful file system assistant. You interpret natural language requests and turn them into specific tool calls. You do not execute the tools yourself; you only output the function calls. If a request is vague, ask for clarification. If the user asks to move or copy 'all files' without a specific extension or criteria, ask for confirmation or clarification to avoid moving system files."},
        {"role": "user", "content": user_prompt}
    ]

    payload = {
        "model": GEMINI_MODEL,
        "messages": messages,
    }

    if tools_schema:
        payload["tools"] = tools_schema
        payload["tool_choice"] = "auto"

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        error_msg = str(e)
        if hasattr(e, 'response') and e.response is not None:
             error_msg += f"\nResponse Body: {e.response.text}"
        return {"error": error_msg}

def parse_llm_response(response_data):
    """
    Extracts the tool calls or content from the LLM response.
    """
    if "error" in response_data:
        return {"error": response_data["error"]}

    try:
        choice = response_data["choices"][0]
        message = choice["message"]
        
        # Check for tool_calls
        if "tool_calls" in message:
            return {"type": "tool_calls", "content": message["tool_calls"]}
        else:
            return {"type": "message", "content": message.get("content", "")}
            
    except (KeyError, IndexError) as e:
        return {"error": f"Unexpected response format: {e}", "raw": response_data}
