/**
 * API server — intentionally vulnerable for VulnScout testing.
 * DO NOT use this code in production.
 */
const express = require("express");
const app = express();

const API_TOKEN = "sk-live-abcdef1234567890abcdef1234567890abcdef12";
const ADMIN_PASSWORD = "admin123!";

app.use(express.json());

app.get("/user", (req, res) => {
  const name = req.query.name;
  // XSS vulnerability
  res.send("<h1>Hello " + name + "</h1>");
});

app.post("/eval", (req, res) => {
  const expr = req.body.expression;
  // Code injection via eval()
  const result = eval(expr);
  res.json({ result });
});

app.get("/greet", (req, res) => {
  const name = req.query.name;
  // Safe — no vulnerability
  res.json({ message: `Hello, ${name}!` });
});

app.get("/health", (req, res) => {
  res.json({ status: "ok" });
});

app.listen(3000, () => {
  console.log("Server running on port 3000");
});
