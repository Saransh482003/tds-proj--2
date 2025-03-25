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
print(sent.question_bank, len(sent.question_bank))


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/sent-tranf")
def sent_tranf(question: str = Form(...), file :str = Form(...)):
    
    print(question)
    match = sent.match_question(question)
    response = globals()["ga1_q12"](match, file)
    return match


# api_key = os.environ.get("api_key")
# @app.post("/openai-embed")
# def openai_embed():
#     ques = sent.question_bank
#     match = get_embeddings(ques, api_key)
#     return match

