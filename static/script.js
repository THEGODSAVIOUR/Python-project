function generateInputs() {
    const count = document.getElementById('count').value;
    const container = document.getElementById('inputFields');
    container.innerHTML = "";

    for (let i = 0; i < count; i++) {
        container.innerHTML += `
            <div>
                <label>Air Temp (°C) ${i + 1}:</label>
                <input type="number" name="air${i}" min="23" max="28" required>
                <label>Dew Point (°C) ${i + 1}:</label>
                <input type="number" name="dew${i}" min="7" max="16" required>
            </div>
        `;
    }
}
