def chunk_text(
    text: str,
    chunk_size: int = 800,
    overlap: int = 150
) -> list[str]:
    """Simple sliding-window chunker."""
    text = text.strip()
    if not text:
        return []

    chunks = []
    start = 0
    n = len(text)

    while start < n:
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap  # move window with overlap

        if start < 0:
            break

    return chunks
