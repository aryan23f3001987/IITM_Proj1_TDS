from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ Enable CORS for all origins (or specify the exact domain if you know it)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],           # Accept requests from any origin
    allow_credentials=True,
    allow_methods=["*"],           # Allow GET, POST, etc.
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return JSONResponse({"message": "TDS Virtual TA API is live. Use POST /api with a question."})

@app.post("/api")
async def answer_question(request: Request):
    data = await request.json()
    question = data.get("question", "")
    image = data.get("image", "")

    # 🛑 Replace this with your real RAG logic
    answer = "This is a placeholder answer. Replace with your model output."
    links = [
        {
            "url": "https://discourse.onlinedegree.iitm.ac.in/t/example/123",
            "text": "Example link"
        }
    ]

    return JSONResponse({"answer": answer, "links": links})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=10000)