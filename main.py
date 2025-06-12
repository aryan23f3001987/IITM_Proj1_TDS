from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Define the expected structure of the input
class QuestionRequest(BaseModel):
    question: str
    image: Optional[str] = ""

# GET endpoint to confirm API is live
@app.get("/api")
def welcome():
    return JSONResponse(content={
        "message": "Welcome to the TDS Virtual TA API. Please send a POST request with 'question' and optional base64 'image'."
    })

# POST endpoint to process questions
@app.post("/api")
async def answer_question(payload: QuestionRequest):
    question = payload.question
    image = payload.image

    # Dummy logic — replace this with your RAG-based answering logic
    answer = "This is a placeholder answer. Replace this with your model output."

    links = [
        {
            "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/4",
            "text": "Use the model that’s mentioned in the question."
        },
        {
            "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/3",
            "text": "Tokenizer-based cost calculation."
        }
    ]

    return JSONResponse(content={
        "answer": answer,
        "links": links
    })
