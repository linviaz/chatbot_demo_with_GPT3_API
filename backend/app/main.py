# fastapi wrapping of openai api

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
import os
import openai
from pydantic import BaseModel

app = FastAPI()

# CORS - cross-origin resource sharing
# when frontend running in a browser has javascript code that communicates with a backend
# and the backend is in a different "origin" from the frontend
origins = [
    "http://localhost",
    "http://localhost:8000",
    "https://127.0.1.1:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=['POST'],
    allow_headers=["*"],
)


# structure frontend input
class FrontendInput(BaseModel):
    sender: str
    message: str


@app.post("/webhook")
async def webhook(prompt: FrontendInput):

    # load open ai api key
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # openai api completion
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt.message,
        temperature=0.5,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices