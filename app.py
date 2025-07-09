import os
import json
import httpx
from fastapi import FastAPI
from datetime import datetime
from pydantic import BaseModel

app = FastAPI()

LOG_FILE = 'logs/log.jsonl'
MODEL_URL = 'http://localhost:11434/api/generate'

os.makedirs('logs', exist_ok=True)


class PromptRequest(BaseModel):
    prompt: str 

class ResponseModel(BaseModel):
    response: str


def log_interaction(prompt: str, response: str):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "prompt": prompt,
        "response": response
    }

    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {"logs": []}
    else:
        data = {"logs": []}

    data["logs"].append(log_entry)

    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=2)


async def query_ollama(prompt: str, model: str = "gemma:2b") -> str:
    url = MODEL_URL
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    # Set a longer timeout for Ollama requests (30 seconds)
    timeout = httpx.Timeout(30.0)
    async with httpx.AsyncClient(timeout=timeout) as client:
        res = await client.post(url, json=payload)
        res.raise_for_status()
        return res.json()["response"]


@app.post('/generate', response_model=ResponseModel)
async def generate_response(request: PromptRequest):
    response_text = await query_ollama(request.prompt)
    log_interaction(request.prompt, response_text)
    return {"response": response_text}
