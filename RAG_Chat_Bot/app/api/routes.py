from fastapi import APIRouter
from app.schemas.request import QueryRequest
from app.rag.pipeline import get_answer

router = APIRouter()

@router.post("/ask")
def ask_bot(request: QueryRequest):
    answer = get_answer(request.query)
    return {"answer": answer}
