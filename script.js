function analyzeRainfall() {
  // Sample rainfall data (in mm)
  const rainfall = [78, 102, 45, 130, 95, 88, 60, 110, 55];
  
  // Sort data (ascending)
  const sorted = [...rainfall].sort((a, b) => a - b);
  
  // Compute average
  const avg = (sorted.reduce((a, b) => a + b, 0) / sorted.length).toFixed(2);
  
  // Basic "prediction" (next rainfall ~ last average ± 10%)
  const predicted = (avg * 1.1).toFixed(2);

  document.getElementById("output").textContent =
    `Original Data: ${rainfall.join(", ")}\n` +
    `Sorted Data: ${sorted.join(", ")}\n` +
    `Average Rainfall: ${avg} mm\n` +
    `Predicted Next Rainfall: ~${predicted} mm`;
}
