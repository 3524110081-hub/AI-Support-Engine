
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Literal

from app.engines.traditional import TraditionalEngine
from app.engines.generative import GenerativeEngine
from app.application.schemas import SupportResponse


app = FastAPI(
    title="AI Support Engine",
    description="API para clasificar solicitudes de soporte mediante IA tradicional y generativa.",
    version="1.0.0"
)


class AnalyzeRequest(BaseModel):
    message: str = Field(
        min_length=1,
        max_length=5000,
        description="Mensaje de soporte que se desea analizar."
    )

    mode: Literal["traditional", "generative"] = "traditional"


traditional_engine = TraditionalEngine()
generative_engine = None


@app.get("/")
def home():
    return {
        "message": "AI Support Engine API funcionando",
        "version": "1.0.0"
    }


@app.post("/api/analyze", response_model=SupportResponse)
def analyze_support(request: AnalyzeRequest):

    global generative_engine

    try:
        if request.mode == "traditional":
            result = traditional_engine.analyze(request.message)

        else:
            if generative_engine is None:
                generative_engine = GenerativeEngine()

            result = generative_engine.analyze(request.message)

        return result

    except Exception as error:
        raise HTTPException(
            status_code=503,
            detail="No fue posible procesar la solicitud. Intente nuevamente."
        ) from error
