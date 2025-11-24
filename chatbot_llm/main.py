from fastapi import FastAPI
from pydantic import BaseModel
from agent import answer_question

class QuestionRequest(BaseModel):
    question: str
    pg_uri: str
    groq_api_key: str

app = FastAPI()

@app.post("/ask")
def ask(req: QuestionRequest):
    return {"answer": answer_question(req.question, req.pg_uri, req.groq_api_key)}
