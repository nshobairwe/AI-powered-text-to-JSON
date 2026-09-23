from typing import Optional

from pydantic import BaseModel, Field


class ExtractedInformation(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = Field(default=None, ge=0, le=150)
    location: Optional[str] = None
    profession: Optional[str] = None
    skills: list[str] = []
    email: Optional[str] = None
    phone: Optional[str] = None
    education: Optional[str] = None
    job_interest: Optional[str] = None
    summary: str
