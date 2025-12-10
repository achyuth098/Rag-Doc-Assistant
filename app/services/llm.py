import requests
from app.config.settings import OLLAMA_URL, OLLAMA_MODEL

def generate_with_ollama(prompt: str) -> str:
    """
    Calls local Ollama (llama3) and returns the full response text.
    """
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    }

    resp = requests.post(OLLAMA_URL, json=payload, timeout=300)
    resp.raise_for_status()
    data = resp.json()
    return data.get("response", "")
