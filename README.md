# Customer Support Ticket Classification System

## 1. Project Overview
This project is an AI/ML-based system that automatically classifies customer
support tickets into predefined categories based on the ticket description.
It includes a machine learning pipeline (data cleaning, EDA, model training,
evaluation), a REST API backend, a React-based web interface for testing
predictions, and an optional AI-generated auto-response feature.

## 2. Problem Statement
Support teams receive tickets through multiple channels (email, chat, etc.).
Manually reading and categorizing each ticket is slow and inconsistent. This
system predicts a ticket's category directly from its description text,
enabling faster routing and response.

## 3. Technologies Used

**Backend**
- Python 3.x
- FastAPI (REST API)
- Pandas, NumPy (data processing)
- Matplotlib, Seaborn (visualization)
- Scikit-learn (TF-IDF + Logistic Regression)
- Groq API (Qwen model) for optional AI-generated responses

**Frontend**
- React (Vite)

## 4. Dataset Information
- File: `backend/data/tickets.csv`
- Records: ~200 tickets
- Categories: Login Issue, Application Error, Report, Account Update, Performance
- Fields: `ticket_id`, `ticket_description`, `category`, `priority`, `status`
- Source: Synthetically generated using Google Gemini (see report.pdf for full prompt used)
## 5. Installation Steps

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate      # on Windows: venv\Scripts\activate
pip install -r requirements.txt
```

GROQ_API_KEY=your_groq_api_key_here


### Frontend Setup
```bash
cd frontend
npm install
```

## 6. How to Train the Model
```bash
cd backend/src
python train.py
```
This cleans the dataset, trains the model, prints evaluation metrics, and
saves `model.pkl` and `vectorizer.pkl` to `backend/model/`.

## 7. How to Run Exploratory Data Analysis
```bash
cd backend/src
python eda.py
```
Generates category/priority/status distribution charts into `screenshots/`.

## 8. How to Test Predictions (CLI)
```bash
cd backend/src
python predict.py
```
Runs 5 sample unseen tickets through the trained model and prints predictions.

## 9. How to Run the Full Application

**Start the backend:**
```bash
cd backend
python app.py
```
API will be available at `http://localhost:8000`.

**Start the frontend (in a separate terminal):**
```bash
cd frontend
npm run dev
```
Open the URL shown (typically `http://localhost:5173`) in your browser.

## 10. Sample Input/Output

**Input:**

I forgot my password and cannot login


**Output:**
Predicted Category: Login Issue
Confidence: 91.4%
Suggested Response: Please use the "Forgot Password" option on the login
page to reset your credentials. If the issue persists, contact our support team.


## 12. Notes
- The `/predict` endpoint runs classification using a locally trained model
  (TF-IDF + Logistic Regression) — always available, no external dependency.
- The AI-generated suggested response uses the Groq API (Qwen model) and
  falls back to a rule-based response if the API is unavailable.
- No API keys or credentials are included in this submission.