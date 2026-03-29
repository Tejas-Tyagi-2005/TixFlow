from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import logging

from utils.preprocess import clean_text
from utils.mapping import map_output

app = FastAPI()

logging.basicConfig(level=logging.INFO)

# Load model from model folder
model = joblib.load("model/model_v2.pkl")
vectorizer = joblib.load("model/vectorizer_v2.pkl")

class Ticket(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/predict")
def predict(ticket: Ticket):
    if not ticket.text.strip():
        raise HTTPException(status_code=400, detail="Empty input")

    try:
        logging.info(f"Input: {ticket.text}")

        cleaned = clean_text(ticket.text)
        vector = vectorizer.transform([cleaned])
        category = model.predict(vector)[0]

        team, priority = map_output(category)

        logging.info(f"Prediction: {category}")

        return {
            "input": ticket.text,
            "prediction": {
                "category": category,
                "team": team,
                "priority": priority
            }
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))