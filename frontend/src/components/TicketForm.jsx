
import { useState } from "react";

function TicketForm({ onSubmit, loading }) {
  const [description, setDescription] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (description.trim() === "") return;
    onSubmit(description);
  };

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="ticket-description">Ticket Description</label>
      <textarea
        id="ticket-description"
        rows={4}
        value={description}
        onChange={(e) => setDescription(e.target.value)}
        placeholder="e.g. I cannot login to the application"
      />
      <button type="submit" disabled={loading || description.trim() === ""}>
        {loading ? "Predicting..." : "Predict"}
      </button>
    </form>
  );
}

export default TicketForm;