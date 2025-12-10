from sentence_transformers import SentenceTransformer

# Small, fast model; good enough for RAG
_model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_text(text: str) -> list[float]:
    return _model.encode([text])[0].tolist()

def embed_text_batch(texts: list[str]) -> list[list[float]]:
    return _model.encode(texts).tolist()
