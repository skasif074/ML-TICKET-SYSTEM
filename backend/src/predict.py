
import os
import joblib

from preprocessing import clean_text

MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "model")
MODEL_PATH = os.path.join(MODEL_DIR, "model.pkl")
VECTORIZER_PATH = os.path.join(MODEL_DIR, "vectorizer.pkl")

_model = None
_vectorizer = None


def _load_artifacts():
    global _model, _vectorizer
    if _model is None or _vectorizer is None:
        _model = joblib.load(MODEL_PATH)
        _vectorizer = joblib.load(VECTORIZER_PATH)
    return _model, _vectorizer


def predict_category(description: str) -> dict:
    model, vectorizer = _load_artifacts()

    cleaned = clean_text(description)
    vectorized = vectorizer.transform([cleaned])

    predicted_label = model.predict(vectorized)[0]
    probabilities = model.predict_proba(vectorized)[0]
    confidence = max(probabilities)

    return {
        "category": predicted_label,
        "confidence": round(float(confidence) * 100, 2),
    }


if __name__ == "__main__":
    test_cases = [
        "I forgot my password and cannot login",
        "The application shows an error while saving data",
        "Need my monthly sales report",
        "I want to update my registered mobile number",
        "The app is extremely slow today",
    ]

    for ticket in test_cases:
        result = predict_category(ticket)
        print(f"Input: {ticket}")
        print(f"Predicted Category: {result['category']}")
        print(f"Confidence: {result['confidence']}%\n")