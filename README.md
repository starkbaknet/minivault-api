# MiniVault API

A lightweight, fully local REST API for interacting with a small language model (LLM) like `gemma` using [Ollama](https://ollama.com). This project supports basic prompt-response interaction and logs all inputs/outputs in a structured JSON file.

---

## Features

- Local-only inference (no cloud, no OpenAI)
- Uses [Ollama](https://ollama.com) to run LLMs like `gemma`, `tinyllama`, or `llama2`
- Simple POST endpoint `/generate`
- Logs all interactions to `logs/log.json` in structured format
- FastAPI-powered, easy to extend

---

## Project Structure

```
minivault-api/
├── app.py              # FastAPI app with endpoint and logging
├── logs/
│   └── log.json        # All prompt/response logs stored here
├── requirements.txt    # Dependencies
└── README.md           # You are here
```

---

## Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/youruser/minivault-api.git
cd minivault-api
```

### 2. Install Python dependencies

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Install and run Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Then pull a lightweight model:

```bash
ollama pull gemma
```

And run it:

```bash
ollama run gemma
```

### 4. Run the API

```bash
uvicorn app:app --reload
```

---

## API Usage

### Endpoint: `POST /generate`

#### Request Body:

```json
{
  "prompt": "Tell me a joke."
}
```

#### Response:

```json
{
  "response": "Sure! Why don't scientists trust atoms? Because they make up everything!"
}
```

---

## Logging

All prompt/response interactions are saved in:

```
logs/log.json
```

The structure looks like:

```json
{
  "logs": [
    {
      "timestamp": "2025-07-08T18:23:45.123Z",
      "prompt": "Hello",
      "response": "Hi there!"
    }
  ]
}
```

---

## Configuration

- **Model**: Default is `"gemma"`, but you can change it inside `query_ollama()` in `app.py`.
- **Log file**: Defaults to `logs/log.json`.

---

## Dependencies

```
fastapi
uvicorn
httpx
```

Install them via:

```bash
pip install -r requirements.txt
```

---

## Notes

- This API does not support streaming — response is returned in full.
- No authentication is implemented — secure it before public exposure.
- You can swap `gemma` with any other supported Ollama model like `llama2`, `tinyllama`, etc.

---

## Example with `curl`

```bash
curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "What is FastAPI?"}'
```

Response

```json
{
  "response": "FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints."
}
```
