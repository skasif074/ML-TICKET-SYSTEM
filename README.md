# Customer Support Ticket Classification System

## Live Demo
- App: https://ml-ticket-system.vercel.app/

**Note:** The backend is hosted on Render's free tier and may take 30–60 seconds to wake up if it has been idle. The frontend shows a loading screen while this happens.

## GitHub Repository
https://github.com/skasif074/ML-TICKET-SYSTEM

## 1. Project Overview
This project is an AI/ML-based system that automatically classifies customer support tickets into predefined categories based on the ticket description. It includes a machine learning pipeline (data cleaning, EDA, model training, evaluation), a REST API backend, a React-based web interface for testing predictions, and an optional AI-generated auto-response feature.

## 2. Problem Statement
Support teams receive tickets through multiple channels (email, chat, etc.). Manually reading and categorizing each ticket is slow and inconsistent. This system predicts a ticket's category directly from its description text, enabling faster routing and response.

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

**Deployment**
- Frontend: Vercel
- Backend: Render

## 4. Dataset Information
- File: backend/data/tickets.csv
- Records: ~200 tickets (180 after cleaning)
- Categories: Login Issue, Application Error, Report, Account Update, Performance
- Fields: ticket_id, ticket_description, category, priority, status
- Source: Synthetically generated using Google Gemini (see report.pdf for full prompt used)

## 5. Installation Steps

### Backend Setup
cd backend
python -m venv venv
source venv/bin/activate      # on Windows: venv\Scripts\activate
pip install -r requirements.txt

Create a .env file inside backend/ (copy from .env.example) containing:
GROQ_API_KEY=your_groq_api_key_here

Get a free key from https://console.groq.com/

### Frontend Setup
cd frontend
npm install

## 6. How to Train the Model
cd backend/src
python train.py

This cleans the dataset, trains the model, prints evaluation metrics, saves model.pkl/vectorizer.pkl to backend/model/, and generates a confusion matrix chart in screenshots/.

## 7. How to Run Exploratory Data Analysis
cd backend/src
python eda.py

Generates category/priority/status distribution charts into screenshots/.

## 8. How to Test Predictions (CLI)
cd backend/src
python predict.py

Runs 5 sample unseen tickets through the trained model and prints predictions.

## 9. How to Run the Full Application Locally

Start the backend:
cd backend
python app.py

API will be available at http://localhost:8000.

Start the frontend (in a separate terminal):
cd frontend
npm run dev

Open the URL shown (typically http://localhost:5173) in your browser.

## 10. Sample Input/Output

Input:
I forgot my password and cannot login

Output:
Predicted Category: Login Issue
Confidence: 91.4%
Suggested Response: Please use the "Forgot Password" option on the login page to reset your credentials. If the issue persists, contact our support team.

## 11. Notes
- The /predict endpoint runs classification using a locally trained model (TF-IDF + Logistic Regression) — always available, no external dependency.
- The AI-generated suggested response uses the Groq API (Qwen model) and falls back to a rule-based response if the API is unavailable.
- No API keys or credentials are included in this submission.
- Live source code and deployment links are provided above for direct testing without local setup.