from pydantic import BaseModel, Field

class TextRequest(BaseModel):
    text: str = Field(..., min_length=10, description="Tesk sumber yang akan diproses")

class SummaryResponse(BaseModel):
    detected_language: str
    original_length: int
    summary_length: int
    summary: str

class KeywordResponse(BaseModel):
    detected_language: str
    keywords: list[str]