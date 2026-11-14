from fastapi import APIRouter
from models.investigation import AskRequest

router = APIRouter()

@router.post("/ask")
def ask_si(payload: AskRequest):
    return {"answer": f"SI synthesis for: {payload.question}", "environment": payload.environment}
