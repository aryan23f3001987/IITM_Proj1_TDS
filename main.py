from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root_get():
    return {"message": "TDS Virtual TA API is live. Send a POST to / with 'question' and optional 'image'."}

@app.post("/")
async def root_post(request: Request):
    data = await request.json()
    question = data.get("question", "")
    image = data.get("image", "")

    # 🔧 Replace with actual logic
    answer = "This is a placeholder answer. Replace with your RAG model's output."
    links = [
        {
            "url": "https://discourse.onlinedegree.iitm.ac.in/t/example/123",
            "text": "Relevant Discourse post"
        }
    ]
    return JSONResponse(content={"answer": answer, "links": links})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=10000)