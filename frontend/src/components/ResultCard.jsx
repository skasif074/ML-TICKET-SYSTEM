// ResultCard.jsx
// Purpose: Displays the prediction result (category, confidence, and the
// AI-generated suggested response) after a successful API call. Renders
// nothing if there is no result yet.

function ResultCard({ result, error }) {
  if (error) {
    return (
      <div className="result-card result-card--error">
        <p>Error: {error}</p>
      </div>
    );
  }

  if (!result) return null;

  return (
    <div className="result-card">
      <h3>Predicted Category</h3>
      <p className="category">{result.category}</p>

      <h3>Confidence</h3>
      <p className="confidence">{result.confidence}%</p>

      <h3>Suggested Response</h3>
      <p className="suggested-response">{result.suggested_response}</p>
    </div>
  );
}

export default ResultCard;