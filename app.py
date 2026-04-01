from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import logging

from utils.preprocess import clean_text
from utils.mapping import map_output

# -------------------------
# APP INIT
# -------------------------
app = FastAPI()

# -------------------------
# CORS 
# -------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# LOGGING
# -------------------------
logging.basicConfig(level=logging.INFO)

# -------------------------
# LOAD MODEL
# -------------------------
model = joblib.load("model/model_v2.pkl")
vectorizer = joblib.load("model/vectorizer_v2.pkl")

# -------------------------
# SCHEMA
# -------------------------
class Ticket(BaseModel):
    text: str

# -------------------------
# ROOT
# -------------------------
@app.get("/")
def home():
    return {"message": "API is running"}

# -------------------------
#  FORCE HANDLE OPTIONS 
# -------------------------
@app.options("/{full_path:path}")
async def options_handler(full_path: str):
    return {"message": "OK"}

# -------------------------
# PREDICT
# -------------------------
@app.post("/predict")
def predict(ticket: Ticket):
    if not ticket.text.strip():
        raise HTTPException(status_code=400, detail="Empty input")

    try:
        cleaned = clean_text(ticket.text)
        vector = vectorizer.transform([cleaned])
        category = model.predict(vector)[0]

        team, priority = map_output(category)

        return {
            "input": ticket.text,
            "prediction": {
                "category": category,
                "team": team,
                "priority": priority
            }
        }

    except Exception as e:
        logging.error(str(e))
        raise HTTPException(status_code=500, detail="Internal Server Error")
