const API_BASE_URL = import.meta.env.DEV
  ? "http://localhost:8000"
  : "https://ml-ticket-system.onrender.com";

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

export async function checkBackendHealth() {
  try {
    const response = await fetch(`${API_BASE_URL}/`, { method: "GET" });
    return response.ok;
  } catch {
    return false;
  }
}