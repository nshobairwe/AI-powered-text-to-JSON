# 🏠 AI Property Inquiry Analyzer

An AI application that converts natural-language property inquiries
into validated structured JSON using Llama 3.2, Ollama, FastAPI,
Pydantic, and Streamlit.

## Architecture

Streamlit → FastAPI → Ollama → Llama 3.2
                         ↓
                  JSON Schema
                         ↓
                Pydantic Validation

## Features

- Natural language property inquiry analysis
- Open-source LLM using Llama 3.2
- Local inference using Ollama
- JSON Schema structured output
- Pydantic validation
- FastAPI REST API
- Streamlit frontend
- Automated tests
- Swagger API documentation

## Example Input

Natafuta nyumba ya vyumba 3 Dar es Salaam
yenye bajeti ya milioni 100.

## Example Output

```json
{
  "intent": "property_search",
  "location": "Dar es Salaam",
  "property_type": "house",
  "bedrooms": 3,
  "budget": 100000000,
  "currency": "TZS",
  "summary": "..."
}
