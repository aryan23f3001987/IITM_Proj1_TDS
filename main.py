from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from utils.rag_search import answer_question

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str
    image: Optional[str] = None  # base64 encoded image string (optional)

@app.post("/api/")
async def ask_virtual_ta(request: QuestionRequest):
    try:
        response = answer_question(request.question, request.image)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))