from flask import Flask, render_template, request
import math

app = Flask(__name__)

def calculate_humidity(air_temp, dew_temp):
    """Calculate relative humidity based on given formulas."""
    specific_humidity = 6.11 * (10 ** ((7.5 * dew_temp) / (237.3 + dew_temp)))
    saturation_point = 6.11 * (10 ** ((7.5 * air_temp) / (237.3 + air_temp)))
    relative_humidity = (specific_humidity / saturation_point) * 100
    return relative_humidity


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        n = int(request.form['count'])
        readings = []

        # Collect readings from form
        for i in range(n):
            air = float(request.form[f'air{i}'])
            dew = float(request.form[f'dew{i}'])
            rh = calculate_humidity(air, dew)
            readings.append((rh, air, dew))

        # Sort by relative humidity (ascending)
        readings.sort(key=lambda x: x[0])

        # Find highest relative humidity
        highest = readings[-1]
        prediction = "Low chance of rainfall."

        # Check if temperature is dropping compared to previous reading
        if highest[0] > 80 and n > 1 and highest[1] < readings[-2][1]:
            prediction = "High chance of rainfall (humidity high & temperature dropping)."

        return render_template(
            'result.html',
            readings=readings,
            highest=highest,
            prediction=prediction
        )

    except Exception as e:
        return f"Error: {e}"


if __name__ == '__main__':
    app.run(debug=True)
