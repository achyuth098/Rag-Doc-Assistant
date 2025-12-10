from typing import List, Tuple, Dict, Any

from app.db.vector_store import get_collection
from app.services.embeddings import embed_text
from app.services.llm import generate_with_ollama

def retrieve_context(
    query: str,
    k: int = 5
) -> List[Tuple[str, Dict[str, Any]]]:
    coll = get_collection()
    q_emb = embed_text(query)

    res = coll.query(
        query_embeddings=[q_emb],
        n_results=k
    )

    docs = res.get("documents", [[]])[0]
    metas = res.get("metadatas", [[]])[0]

    return list(zip(docs, metas))

def build_prompt(query: str, context_docs: List[Tuple[str, Dict[str, Any]]]) -> str:
    context_text = "\n\n".join(
        f"[{i}] (source: {m.get('source', 'unknown')})\n{d}"
        for i, (d, m) in enumerate(context_docs)
    )

    return f"""
You are an assistant answering questions based only on the provided context.

CONTEXT:
{context_text}

USER QUESTION:
{query}

INSTRUCTIONS:
- Answer using the CONTEXT as much as possible.
- If the answer is not in the context, say you don't know.
- Be concise and structured.
"""

def answer_question(query: str) -> dict:
    ctx = retrieve_context(query)
    prompt = build_prompt(query, ctx)
    answer = generate_with_ollama(prompt)
    return {
        "answer": answer.strip(),
        "context": ctx
    }
