from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        n = int(request.form['n'])
        data = []

        for i in range(1, n + 1):
            air_temp = float(request.form[f'air_temp_{i}'])
            dew_temp = float(request.form[f'dew_temp_{i}'])

            # Calculations
            specific_humidity = 6.11 * 10 ** ((7.5 * dew_temp) / (237.3 + dew_temp))
            saturation_point = 6.11 * 10 ** ((7.5 * air_temp) / (237.3 + air_temp))
            relative_humidity = (specific_humidity / saturation_point) * 100

            data.append({
                'air_temp': air_temp,
                'dew_temp': dew_temp,
                'humidity': round(relative_humidity, 2)
            })

        # Sort by humidity
        sorted_data = sorted(data, key=lambda x: x['humidity'])

        # Highest humidity
        highest = sorted_data[-1]
        prediction = "High" if highest['humidity'] > 70 and highest['air_temp'] < 26 else "Low"

        return render_template(
            'result.html',
            sorted_data=sorted_data,
            highest=highest,
            prediction=prediction
        )

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
