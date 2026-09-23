from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from ollama import chat

from backend.schema import ExtractedInformation

app = FastAPI(
    title="AI Text-to-JSON Extractor",
    description="Extract structured information from user-provided text using Llama 3.2",
    version="1.0.0",
)


class TextRequest(BaseModel):
    text: str


SYSTEM_PROMPT = """
You are an information extraction assistant.

Your task is to extract structured information from the
user-provided text.

Rules:

1. Extract only information explicitly provided in the text
2. Do not invent or guess information
3. If a field is not available, return null
4. Extract skills as a list of strings
5. Age must be a number
6. Keep the summary short and factual
7. Return the information according to the provided JSON schema
"""


@app.get("/")
def root():
    return {"message": "AI Text-to-JSON Extractor is running"}


@app.get("/schema")
def get_schema():
    return ExtractedInformation.model_json_schema()


@app.post("/extract", response_model=ExtractedInformation)
def extract_information(request: TextRequest):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    try:
        response = chat(
            model="llama3.2",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": request.text},
            ],
            format=ExtractedInformation.model_json_schema(),
        )

        raw_output = response.message.content
        result = ExtractedInformation.model_validate_json(raw_output)
        return result
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"AI Extraction failed: {str(e)}",
        ) from e