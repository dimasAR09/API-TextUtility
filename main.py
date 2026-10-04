from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    tittle="Text Utility Pro API", 
    description="API utilitas pemrosesan teks untuk RapidAPI",
    version="1.0.0"
)

app.include_router(router, prefix="/api/v1")

@app.get("/")
def health_check():
    return {"status": "Active", "message": "API siap melayani permintaan."}