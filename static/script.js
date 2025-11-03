document.getElementById('addRow').addEventListener('click', () => {
  const container = document.getElementById('input-container');
  const newGroup = document.createElement('div');
  newGroup.classList.add('input-group', 'fade-in');

  newGroup.innerHTML = `
    <label>🌡 Temperature (°C):</label>
    <input type="number" name="temp" step="0.1" required>

    <label>💧 Dew Point (°C):</label>
    <input type="number" name="dew" step="0.1" required>
  `;
  
  container.appendChild(newGroup);
});
