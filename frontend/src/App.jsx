// App.jsx
// Purpose: Root component of the application. Holds the prediction result
// and loading/error state, renders the ticket form and result card, and
// calls the backend API when the user submits a ticket description.

import { useState } from "react";
import TicketForm from "./components/TicketForm";
import ResultCard from "./components/ResultCard";
import { predictTicketCategory } from "./api";
import "./App.css";

function App() {
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const handlePredict = async (description) => {
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const data = await predictTicketCategory(description);
      setResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <h1>Customer Support Ticket Classifier</h1>
      <TicketForm onSubmit={handlePredict} loading={loading} />
      <ResultCard result={result} error={error} />
    </div>
  );
}

export default App;