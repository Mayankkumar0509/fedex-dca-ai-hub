async function predict() {
  const data = {
    amount_due: Number(document.getElementById("amount").value),
    days_overdue: Number(document.getElementById("days").value),
    customer_risk_score: Number(document.getElementById("risk").value),
    past_recovery_rate: Number(document.getElementById("past").value)
  };

  const response = await fetch("https://fedex-dca-ai-hub.onrender.com/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });

  const result = await response.json();

  document.getElementById("result").innerText =
    `Recovery Probability: ${result.recovery_probability}
     | Priority Score: ${result.priority_score}
     | Priority Level: ${result.priority_level}`;
}
