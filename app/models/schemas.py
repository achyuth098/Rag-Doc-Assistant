from pydantic import BaseModel
from typing import Any, Dict, List

class AskRequest(BaseModel):
    query: str

class Source(BaseModel):
    text: str
    metadata: Dict[str, Any]

class AskResponse(BaseModel):
    answer: str
    sources: List[Source]
