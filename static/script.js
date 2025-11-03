document.addEventListener("DOMContentLoaded", () => {
  const analyzeBtn = document.getElementById("analyze-btn");
  const rainfallInput = document.getElementById("rainfall");
  const algorithmSelect = document.getElementById("algorithm");
  const outputDiv = document.getElementById("output");

  analyzeBtn.addEventListener("click", async () => {
    // Get rainfall values from textarea
    const rainfallValues = rainfallInput.value
      .split(",")
      .map(v => parseFloat(v.trim()))
      .filter(v => !isNaN(v));

    if (rainfallValues.length === 0) {
      outputDiv.innerHTML = "<p style='color:red;'>⚠️ Please enter valid rainfall values!</p>";
      return;
    }

    const algorithm = algorithmSelect.value;

    try {
      const response = await fetch("/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          rainfall: rainfallValues,
          algorithm: algorithm
        })
      });

      if (!response.ok) {
        throw new Error("Server error");
      }

      const result = await response.json();

      outputDiv.innerHTML = `
        <h3>Results</h3>
        <p><b>Original Data:</b> ${result.original.join(", ")}</p>
        <p><b>Sorted Data (${algorithm} sort):</b> ${result.sorted_data.join(", ")}</p>
        <p><b>Average Rainfall:</b> ${result.average}</p>
        <p><b>Predicted Next Value:</b> ${result.prediction}</p>
      `;
    } catch (error) {
      console.error(error);
      outputDiv.innerHTML = "<p style='color:red;'>⚠️ Something went wrong while processing data.</p>";
    }
  });
});
