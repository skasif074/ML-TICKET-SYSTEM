import { useState, useRef } from "react";
import TicketForm from "./components/TicketForm";
import ResultCard from "./components/ResultCard";
import { predictTicketCategory } from "./api";
import "./App.css";

function App() {
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);
  const [slowServerNotice, setSlowServerNotice] = useState(false);
  const timeoutRef = useRef(null);

  const handlePredict = async (description) => {
    setLoading(true);
    setError(null);
    setResult(null);
    setSlowServerNotice(false);

    timeoutRef.current = setTimeout(() => {
      setSlowServerNotice(true);
    }, 4000);

    try {
      const data = await predictTicketCategory(description);
      setResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      clearTimeout(timeoutRef.current);
      setSlowServerNotice(false);
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <h1>Customer Support Ticket Classifier</h1>
      <TicketForm onSubmit={handlePredict} loading={loading} />
      {loading && slowServerNotice && (
        <p className="loading-notice">
          Waking up the server, this can take up to a minute on first request...
        </p>
      )}
      <ResultCard result={result} error={error} />
    </div>
  );
}

export default App;