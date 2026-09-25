// api.js
// Purpose: Centralizes all communication with the FastAPI backend so
// components don't need to know request/response details directly.
// If the backend URL or endpoint changes, this is the only file to update.

const API_BASE_URL = "http://localhost:8000";

export async function predictTicketCategory(description) {
  const response = await fetch(`${API_BASE_URL}/predict`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ description }),
  });

  if (!response.ok) {
    const errorData = await response.json().catch(() => ({}));
    throw new Error(errorData.detail || "Failed to get prediction from server");
  }

  return response.json();
}