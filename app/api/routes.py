from fastapi import APIRouter
from app.models.schemas import AskRequest, AskResponse, Source
from app.services.rag import answer_question

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "ok"}

@router.post("/ask", response_model=AskResponse)
def ask(req: AskRequest):
    result = answer_question(req.query)

    sources = [
        Source(text=d, metadata=m)
        for (d, m) in result["context"]
    ]

    return AskResponse(
        answer=result["answer"],
        sources=sources
    )
