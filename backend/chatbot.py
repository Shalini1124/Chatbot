from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)


class Question(BaseModel):
    question: str


CDP_DOCS = {
    "segment": "https://segment.com/docs/",
    "mparticle": "https://docs.mparticle.com/",
    "lytics": "https://docs.lytics.com/",
    "zeotap": "https://docs.zeotap.com/home/en-us/"
}

@app.post("/chat")
async def chatbot_response(question: Question):
    """Handles chatbot questions and returns relevant documentation links."""
    query = question.question.lower()


    if "segment" in query:
        return {"answer": f"Check Segment docs here: {CDP_DOCS['segment']}"}
    elif "mparticle" in query:
        return {"answer": f"Check mParticle docs here: {CDP_DOCS['mparticle']}"}
    elif "lytics" in query:
        return {"answer": f"Check Lytics docs here: {CDP_DOCS['lytics']}"}
    elif "zeotap" in query:
        return {"answer": f"Check Zeotap docs here: {CDP_DOCS['zeotap']}"}
    else:
        return {"answer": "Sorry, I can only answer questions related to Segment, mParticle, Lytics, or Zeotap."}


