from pathlib import Path
from pypdf import PdfReader

from app.db.vector_store import get_collection
from app.services.chunking import chunk_text
from app.services.embeddings import embed_text_batch

RAW_DIR = Path("data/raw")

def extract_text_from_file(path: Path) -> str:
    if path.suffix.lower() == ".pdf":
        reader = PdfReader(str(path))
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    elif path.suffix.lower() in {".txt", ".md"}:
        return path.read_text(encoding="utf-8", errors="ignore")
    else:
        return ""

def main():
    coll = get_collection()

    for file in RAW_DIR.glob("**/*"):
        if not file.is_file():
            continue

        print(f"Processing {file}...")
        text = extract_text_from_file(file)
        if not text.strip():
            print(f"Skipping {file} (no text)")
            continue

        chunks = chunk_text(text)
        if not chunks:
            print(f"Skipping {file} (no chunks)")
            continue

        embeddings = embed_text_batch(chunks)

        ids = [f"{file.name}-{i}" for i in range(len(chunks))]
        metadatas = [
            {"source": str(file), "chunk_index": i}
            for i in range(len(chunks))
        ]

        coll.add(
            ids=ids,
            documents=chunks,
            embeddings=embeddings,
            metadatas=metadatas
        )

        print(f"Ingested {file} ({len(chunks)} chunks)")

if __name__ == "__main__":
    main()
