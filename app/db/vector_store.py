import chromadb
from chromadb.config import Settings as ChromaSettings
from app.config.settings import CHROMA_DIR

client = chromadb.PersistentClient(
    path=CHROMA_DIR,
    settings=ChromaSettings(allow_reset=False)
)

def get_collection(name: str = "docs"):
    return client.get_or_create_collection(name=name)
