import os
import requests
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("OPENROUTER_API_KEY")

try:
    resp = requests.get("https://openrouter.ai/api/v1/models", headers={"Authorization": f"Bearer {key}"})
    if resp.status_code == 200:
        data = resp.json()
        print("Available models:")
        for m in data['data']:
            if 'gemini' in m['id']:
                print(m['id'])
    else:
        print(f"Error: {resp.status_code} {resp.text}")
except Exception as e:
    print(e)
