import { useState, useEffect } from "react";
import TicketForm from "./components/TicketForm";
import ResultCard from "./components/ResultCard";
import { predictTicketCategory, checkBackendHealth } from "./api";
import "./App.css";

const LOADING_MESSAGES = [
  "Developed and Tested by SK Asif",
  "Initial load can take up to 1 minute",
  "Deployed on Render free tier, please standby",
  "First load can take up to 1 minute",
  "Waking up the server...",
];

function App() {
  const [backendReady, setBackendReady] = useState(false);
  const [messageIndex, setMessageIndex] = useState(0);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);
  const [firstPredictionDone, setFirstPredictionDone] = useState(false);

  useEffect(() => {
    let isMounted = true;

    const waitForBackend = async () => {
      const success = await checkBackendHealth();
      if (isMounted && success) {
        setBackendReady(true);
      } else if (isMounted) {
        setTimeout(waitForBackend, 3000);
      }
    };

    waitForBackend();
    return () => {
      isMounted = false;
    };
  }, []);

  useEffect(() => {
    if (backendReady) return;
    const interval = setInterval(() => {
      setMessageIndex((prev) => (prev + 1) % LOADING_MESSAGES.length);
    }, 2200);
    return () => clearInterval(interval);
  }, [backendReady]);

  const handlePredict = async (description) => {
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const data = await predictTicketCategory(description);
      setResult(data);
      setFirstPredictionDone(true);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  if (!backendReady) {
    return (
      <div className="app-container loading-screen">
        <h1>Customer Support Ticket Classifier</h1>
        <div className="spinner"></div>
        <p className="loading-message">{LOADING_MESSAGES[messageIndex]}</p>
      </div>
    );
  }

  return (
    <div className="app-container">
      <h1>Customer Support Ticket Classifier</h1>

      <div className="info-panel">
        <p className="info-title">How to use this tool</p>
        <ul className="info-list">
          <li>Type a customer support ticket description in the box below (e.g. "I can't login to my account")</li>
          <li>Click <strong>Predict</strong> to see the predicted category, confidence score, and an AI-generated suggested reply</li>
          <li>This app is hosted on a free-tier server, so the <strong>first prediction may take 20–30 seconds</strong> while the ML model loads into memory</li>
          <li>Every prediction after the first one will be <strong>instant</strong></li>
        </ul>
      </div>

      <TicketForm onSubmit={handlePredict} loading={loading} />

      {loading && !firstPredictionDone && (
        <div className="predicting-notice">
          <div className="spinner small"></div>
          <p>Loading the model for the first time, please wait...</p>
        </div>
      )}

      <ResultCard result={result} error={error} />
    </div>
  );
}

export default App;