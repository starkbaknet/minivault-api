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

## Design Choices & Future Improvements

This project prioritizes simplicity, speed, and local-first design using FastAPI and Ollama. It avoids cloud dependencies and external storage. In the future, support for streaming responses, multi-model selection, and a `/logs` retrieval endpoint could enhance usability and flexibility.

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
git clone https://github.com/starkbaknet/minivault-api.git
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
  "prompt": "What is FastAPI?."
}
```

#### Response:

```json
{
  "response": "Sure. Here's a breakdown of what FastAPI is:\n\n**FastAPI is an open-source, high-performance web framework for Python that focuses on simplicity and flexibility.** It's built on top of the popular Pydantic library and uses the Starlette web server.\n\n**Here's what makes FastAPI unique:**\n\n* **Focus on developer experience:** It prioritizes developer experience with features like automatic data validation, type hints, and clear error messages.\n* **High performance:** FastAPI is one of the most performant Python web frameworks due to its efficient routing system and caching mechanisms.\n* **Extensible:** It provides a large number of features and extensions for developers to customize their applications.\n* **Well-documented:** The official documentation is comprehensive and easy to understand, making it a great starting point for learning FastAPI.\n\n**Here's how FastAPI can be used:**\n\n* **Web services:** It can be used to build RESTful web services that handle various HTTP methods.\n* **API development:** FastAPI can be used to build both RESTful and GraphQL APIs.\n* **Task scheduling:** It integrates with the `apscheduler` library for scheduling tasks and background processing.\n* **Data manipulation:** It provides support for various data manipulation libraries like `json`, `pandas`, and `orjson`.\n\n**Benefits of using FastAPI:**\n\n* **Reduced boilerplate code:** It minimizes the need for repetitive coding, saving developers time and effort.\n* **Type hints:** It provides type hints for variables and parameters, improving code clarity and reducing errors.\n* **Clear error messages:** It displays clear and informative error messages for easier debugging.\n* **Fast performance:** It's one of the most performant Python web frameworks, ensuring quick response times.\n* **Large community:** It has a large and active community of developers who contribute to its growth and support.\n\n**Overall, FastAPI is a powerful and flexible web framework that can be used to build scalable and performant web applications. It's a great choice for developers who prioritize developer experience, performance, and extensibility.**"
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
      "timestamp": "2025-07-09T05:29:14.765147",
      "prompt": "What is FastAPI?",
      "response": "Sure. Here's a breakdown of what FastAPI is:\n\n**FastAPI is an open-source, high-performance web framework for Python that focuses on simplicity and flexibility.** It's built on top of the popular Pydantic library and uses the Starlette web server.\n\n**Here's what makes FastAPI unique:**\n\n* **Focus on developer experience:** It prioritizes developer experience with features like automatic data validation, type hints, and clear error messages.\n* **High performance:** FastAPI is one of the most performant Python web frameworks due to its efficient routing system and caching mechanisms.\n* **Extensible:** It provides a large number of features and extensions for developers to customize their applications.\n* **Well-documented:** The official documentation is comprehensive and easy to understand, making it a great starting point for learning FastAPI.\n\n**Here's how FastAPI can be used:**\n\n* **Web services:** It can be used to build RESTful web services that handle various HTTP methods.\n* **API development:** FastAPI can be used to build both RESTful and GraphQL APIs.\n* **Task scheduling:** It integrates with the `apscheduler` library for scheduling tasks and background processing.\n* **Data manipulation:** It provides support for various data manipulation libraries like `json`, `pandas`, and `orjson`.\n\n**Benefits of using FastAPI:**\n\n* **Reduced boilerplate code:** It minimizes the need for repetitive coding, saving developers time and effort.\n* **Type hints:** It provides type hints for variables and parameters, improving code clarity and reducing errors.\n* **Clear error messages:** It displays clear and informative error messages for easier debugging.\n* **Fast performance:** It's one of the most performant Python web frameworks, ensuring quick response times.\n* **Large community:** It has a large and active community of developers who contribute to its growth and support.\n\n**Overall, FastAPI is a powerful and flexible web framework that can be used to build scalable and performant web applications. It's a great choice for developers who prioritize developer experience, performance, and extensibility.**"
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
  "response": "Sure. Here's a breakdown of what FastAPI is:\n\n**FastAPI is an open-source, high-performance web framework for Python that focuses on simplicity and flexibility.** It's built on top of the popular Pydantic library and uses the Starlette web server.\n\n**Here's what makes FastAPI unique:**\n\n* **Focus on developer experience:** It prioritizes developer experience with features like automatic data validation, type hints, and clear error messages.\n* **High performance:** FastAPI is one of the most performant Python web frameworks due to its efficient routing system and caching mechanisms.\n* **Extensible:** It provides a large number of features and extensions for developers to customize their applications.\n* **Well-documented:** The official documentation is comprehensive and easy to understand, making it a great starting point for learning FastAPI.\n\n**Here's how FastAPI can be used:**\n\n* **Web services:** It can be used to build RESTful web services that handle various HTTP methods.\n* **API development:** FastAPI can be used to build both RESTful and GraphQL APIs.\n* **Task scheduling:** It integrates with the `apscheduler` library for scheduling tasks and background processing.\n* **Data manipulation:** It provides support for various data manipulation libraries like `json`, `pandas`, and `orjson`.\n\n**Benefits of using FastAPI:**\n\n* **Reduced boilerplate code:** It minimizes the need for repetitive coding, saving developers time and effort.\n* **Type hints:** It provides type hints for variables and parameters, improving code clarity and reducing errors.\n* **Clear error messages:** It displays clear and informative error messages for easier debugging.\n* **Fast performance:** It's one of the most performant Python web frameworks, ensuring quick response times.\n* **Large community:** It has a large and active community of developers who contribute to its growth and support.\n\n**Overall, FastAPI is a powerful and flexible web framework that can be used to build scalable and performant web applications. It's a great choice for developers who prioritize developer experience, performance, and extensibility.**"
}
```
