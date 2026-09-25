// main.jsx
// Purpose: Entry point of the React application. Mounts the App component
// into the root DOM node defined in index.html.

import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);