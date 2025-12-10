from pathlib import Path

# Where Chroma will store its DB
CHROMA_DIR = str(Path("chroma_db").resolve())

# Ollama settings
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3"