// script.js

// Wait for DOM to load
document.addEventListener('DOMContentLoaded', function () {
    const addMoreBtn = document.getElementById('addMore');
    const inputContainer = document.getElementById('inputFields');

    // When user clicks "Add More", duplicate the input fields
    addMoreBtn.addEventListener('click', function () {
        const group = document.createElement('div');
        group.classList.add('input-group');

        group.innerHTML = `
            <label>Air Temperature (°C):</label>
            <input type="number" step="any" name="temp" min="23" max="28" required>
            <label>Dew Point (°C):</label>
            <input type="number" step="any" name="dew" min="7" max="16" required>
        `;

        inputContainer.appendChild(group);
    });
});
