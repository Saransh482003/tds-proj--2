from fastapi import FastAPI, File, Form, UploadFile
from pydantic import BaseModel
from sent_tranf import MatchQuestion
from openai_embed import get_embeddings
import os
from functions import *
import json

app = FastAPI()

class Item(BaseModel):
    name: str
    roll_no: int
    roe_marks: int

with open("question_mapper.json", "r") as f:
    question_mapper = json.load(f)

sent = MatchQuestion()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/api")
async def sent_tranf(question: str = Form(...), file: UploadFile = File(...)):
    match = sent.match_question(question)
    file_bytes = await file.read()
    answer = globals()[question_mapper[match]](question, file_bytes)
    return {"answer": answer}


# api_key = os.environ.get("api_key")
# @app.post("/openai-embed")
# def openai_embed():
#     ques = sent.question_bank
#     match = get_embeddings(ques, api_key)
#     return match

