# 🤖 AI Text-to-JSON Information Extraction System

An AI-powered information extraction system that converts unstructured natural-language text into structured and validated JSON using **Llama 3.2, Ollama, FastAPI, Pydantic, JSON Schema, and Streamlit**.

The system accepts natural-language text, extracts predefined information using a Large Language Model (LLM), generates structured JSON according to a **Pydantic-generated JSON Schema**, and validates the output before returning it to the user.

## 🚀 Project Overview

Large Language Models can understand unstructured human language, but applications often need information in a predictable and machine-readable format.

This project demonstrates how to combine an LLM with **JSON Schema and Pydantic validation** to create reliable structured outputs.

For example, the user can provide:

> My name is Witness. I am 25 years old and I live in Dar es Salaam. I am a Software Developer with skills in Python, Django and FastAPI. I am looking for a Python backend job.

The system extracts the information and produces structured JSON:

```json
{
  "name": "Witness",
  "age": 25,
  "location": "Dar es Salaam",
  "profession": "Software Developer",
  "skills": [
    "Python",
    "Django",
    "FastAPI"
  ],
  "email": null,
  "phone": null,
  "education": null,
  "job_interest": "Python backend job",
  "summary": "Witness is a Software Developer interested in Python backend development."
}
```

## 🏗️ System Architecture

```text
                 User
                  │
                  ▼
          ┌───────────────┐
          │   Streamlit   │
          │   Frontend    │
          └───────┬───────┘
                  │ HTTP Request
                  ▼
          ┌───────────────┐
          │    FastAPI    │
          │    Backend    │
          └───────┬───────┘
                  │
                  ▼
          ┌───────────────┐
          │   Ollama      │
          │ Local Runtime │
          └───────┬───────┘
                  │
                  ▼
          ┌───────────────┐
          │   Llama 3.2   │
          │      LLM      │
          └───────┬───────┘
                  │
                  ▼
          ┌───────────────┐
          │  JSON Schema  │
          │  + Pydantic   │
          └───────┬───────┘
                  │
                  ▼
          Structured & Validated JSON
```

## ✨ Features

* Extract information from unstructured text
* Uses Llama 3.2 locally through Ollama
* Schema-based structured output
* Pydantic data validation
* Automatically generated JSON Schema
* FastAPI REST API
* Interactive Streamlit frontend
* Handles missing information using `null`
* Validates data types and constraints
* Local AI inference without requiring a cloud AI API
* Automated schema validation tests using Pytest

## 🛠️ Technologies

| Technology  | Purpose                               |
| ----------- | ------------------------------------- |
| Python      | Core programming language             |
| Llama 3.2   | Large Language Model                  |
| Ollama      | Local LLM runtime                     |
| FastAPI     | Backend REST API                      |
| Pydantic    | Data modeling and validation          |
| JSON Schema | Defines the expected output structure |
| Streamlit   | Web interface                         |
| Requests    | HTTP communication                    |
| Pytest      | Automated testing                     |

## 📁 Project Structure

```text
ai-text-to-json/
│
├── backend/
│   ├── __init__.py
│   ├── main.py
│   └── schemas.py
│
├── frontend/
│   └── app.py
│
├── tests/
│   └── test_schema.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

## ⚙️ How It Works

### 1. User provides text

The user enters unstructured natural-language text through the Streamlit interface.

### 2. FastAPI receives the request

The frontend sends the text to the FastAPI `/extract` endpoint.

```http
POST /extract
```

### 3. Pydantic defines the data structure

The expected output is defined using a Pydantic model.

```python
class ExtractedInformation(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    location: Optional[str] = None
    profession: Optional[str] = None
    skills: List[str] = []
    email: Optional[str] = None
    phone: Optional[str] = None
    education: Optional[str] = None
    job_interest: Optional[str] = None
    summary: str
```

### 4. JSON Schema is generated

Pydantic generates a JSON Schema from the model:

```python
ExtractedInformation.model_json_schema()
```

This schema defines the expected structure and data types of the AI response.

### 5. Llama 3.2 generates the structured output

The schema is passed to Ollama when calling the model.

```python
response = chat(
    model="llama3.2",
    messages=messages,
    format=ExtractedInformation.model_json_schema()
)
```

### 6. The response is validated

The generated JSON is validated using Pydantic:

```python
result = ExtractedInformation.model_validate_json(
    raw_output
)
```

If the data does not conform to the expected structure, the backend returns an error instead of blindly accepting the response.

## 🔧 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-text-to-json.git
```

```bash
cd ai-text-to-json
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv venv
```

Activate it:

```powershell
venv\Scripts\activate
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

## 🦙 Setup Ollama

Install Ollama and verify that it is available:

```powershell
ollama --version
```

Pull the Llama 3.2 model:

```powershell
ollama pull llama3.2
```

Verify the model:

```powershell
ollama list
```

You can also test the model directly:

```powershell
ollama run llama3.2
```

## ▶️ Running the Application

The project requires two terminals.

### Terminal 1 — Start FastAPI

From the project root:

```powershell
uvicorn backend.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

FastAPI Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

### Terminal 2 — Start Streamlit

```powershell
streamlit run frontend/app.py
```

The Streamlit application will normally be available at:

```text
http://localhost:8501
```

## 🔌 API Endpoints

### `GET /`

Checks whether the API is running.

Example response:

```json
{
  "message": "AI Text-to-JSON Extractor is running"
}
```

### `GET /schema`

Returns the JSON Schema generated from the Pydantic model.

### `POST /extract`

Extracts structured information from natural-language text.

Request:

```json
{
  "text": "John is a software developer who works with Python and Django."
}
```

Response:

```json
{
  "name": "John",
  "age": null,
  "location": null,
  "profession": "Software Developer",
  "skills": [
    "Python",
    "Django"
  ],
  "email": null,
  "phone": null,
  "education": null,
  "job_interest": null,
  "summary": "John is a software developer with experience in Python and Django."
}
```

## 🧪 Testing

The project includes automated tests for the Pydantic schema.

Run:

```powershell
pytest
```

The tests verify cases such as:

* Valid structured data
* Invalid age values
* Invalid data types
* Pydantic validation behavior

## 🔐 Why JSON Schema?

A simple prompt such as:

```text
Return the information as JSON.
```

does not provide strong guarantees about the structure of the response.

With JSON Schema, we can define:

* Expected fields
* Data types
* Optional fields
* Arrays
* Validation constraints
* Expected structure

This makes the AI output easier and safer for backend applications to consume.

## 🧠 Important Concept

**JSON Schema does not guarantee that the extracted information is factually correct.**

It primarily ensures that the response follows the expected structure and data types.

For example, the model could potentially return:

```json
{
  "age": 35
}
```

when the actual person's age is 25.

The JSON may be structurally valid but factually incorrect.

Production systems should therefore combine schema validation with additional validation, trusted data sources, business rules, or human review where necessary.

## 🎯 Use Cases

This architecture can be adapted for:

* CV/resume information extraction
* Customer information extraction
* Document processing
* Job application processing
* Email information extraction
* Support ticket classification
* Invoice data extraction
* Healthcare document processing
* Contract/document analysis
* Automated data-entry systems

## 🔮 Future Improvements

Possible improvements include:

* Add authentication and authorization
* Add database persistence
* Support PDF and DOCX documents
* Add OCR for scanned documents
* Add multiple extraction schemas
* Add confidence scoring
* Add batch document processing
* Add background processing with Celery
* Add Redis for caching and queues
* Add Docker deployment
* Add production monitoring and logging
* Add support for additional local LLMs

## 👩‍💻 Author

**Witness Sostenes Nshobairwe**

Software Engineer | Data Scientist

GitHub: `https://github.com/nshobairwe`

LinkedIn: `https://www.linkedin.com/in/witnes-nshobairwe-9b3580282/`

## 📄 License

This project is intended for educational, portfolio, and demonstration purposes.
