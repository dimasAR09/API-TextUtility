from fastapi import APIRouter, Depends
from app.models.schemas import  TextRequest, SummaryResponse, KeywordResponse
from app.services import text_engine
from app.core.security import verify_rapidapi_header

router = APIRouter(dependencies=[Depends(verify_rapidapi_header)])

@router.post("/summarize", response_model=SummaryResponse)
def summarize_text(payload: TextRequest):
    summary_result, detected_lang = text_engine.generate_summary(payload.text)
    return SummaryResponse(
        detected_language=detected_lang,
        original_length=len(payload.text),
        summary_length=len(summary_result),
        summary=summary_result
    )

@router.post("/keywords", response_model=KeywordResponse)
def get_ketwords(payload: TextRequest):
    keywords_result, detected_lang = text_engine.extract_keywords(payload.text)
    return KeywordResponse(
        detected_language=detected_lang,
        keywords=keywords_result
    )