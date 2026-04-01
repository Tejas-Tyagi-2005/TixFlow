# TixFlow 

ML-powered ticket classification and routing system with FastAPI and AWS deployment.

---

##  Overview

TixFlow is an end-to-end backend system that automatically classifies customer support tickets and routes them to the appropriate team with priority levels.

It combines:
- Machine Learning (text classification)
- FastAPI (backend API)
- AWS EC2 (deployment)

---

##  Features

- Automated ticket classification
- Intelligent routing (team + priority)
- REST API with FastAPI
- Cloud deployment on AWS EC2
- Modular and scalable code structure

---

##  How It Works

1. User sends a ticket (text input)
2. API processes the request
3. Text is cleaned (preprocessing)
4. Converted into features (TF-IDF vectorizer)
5. Model predicts ticket category
6. Category is mapped to:
   - Team
   - Priority
7. JSON response is returned

---

##  Architecture

User → FastAPI → Preprocessing → Vectorizer → Model → Mapping → Response

---

##  API Endpoint

### POST `/predict`

#### Request:
```json
{
  "text": "payment failed and money deducted"
}
