
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from predict import predict_category
from generate_response import generate_response

app = FastAPI(title="Customer Support Ticket Classifier API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://ml-ticket-system.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TicketRequest(BaseModel):
    description: str


class PredictionResponse(BaseModel):
    category: str
    confidence: float
    suggested_response: str


@app.get("/")
def health_check():
    return {"status": "ok", "message": "Ticket Classifier API is running"}


@app.post("/predict", response_model=PredictionResponse)
def predict(ticket: TicketRequest):
    if not ticket.description or not ticket.description.strip():
        raise HTTPException(status_code=400, detail="Ticket description cannot be empty")

    result = predict_category(ticket.description)
    category = result["category"]
    confidence = result["confidence"]

    suggested_response = generate_response(category, ticket.description)

    return PredictionResponse(
        category=category,
        confidence=confidence,
        suggested_response=suggested_response,
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)