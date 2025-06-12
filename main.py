from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def read_root():
    return JSONResponse({"message": "TDS Virtual TA API is live. Use POST /api with a question."})

@app.post("/api")
async def answer_question(request: Request):
    try:
        data = await request.json()
        question = data.get("question", "")
        image = data.get("image", "")

        # Placeholder logic - replace with real model prediction
        answer = "This is a placeholder answer. Replace this with your model output."
        links = [
            {
                "url": "https://discourse.onlinedegree.iitm.ac.in/t/example-post/123456",
                "text": "Example reference link"
            }
        ]

        return JSONResponse({
            "answer": answer,
            "links": links
        })

    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=10000)
