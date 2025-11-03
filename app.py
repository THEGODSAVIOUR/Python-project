from flask import Flask, render_template, request
import math

app = Flask(__name__)

def calculate_humidity(temp, dew):
    specific = 6.11 * 10 ** ((7.5 * dew) / (237.3 + dew))
    saturation = 6.11 * 10 ** ((7.5 * temp) / (237.3 + temp))
    rh = (specific / saturation) * 100
    return rh

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    n = int(request.form['num_readings'])
    temps, dews = [], []
    humidities = []

    for i in range(n):
        t = float(request.form.get(f'air_temp_{i}'))
        d = float(request.form.get(f'dew_point_{i}'))
        h = calculate_humidity(t, d)
        temps.append(t)
        dews.append(d)
        humidities.append(h)

    data = sorted(zip(humidities, temps, dews))

    highest = max(data, key=lambda x: x[0])
    highest_humidity, high_temp, high_dew = highest

    # Prediction rule
    prediction = "High" if highest_humidity > 80 and high_temp < temps[0] else "Low"

    return render_template(
        'result.html',
        data=data,
        highest=highest,
        prediction=prediction
    )

if __name__ == '__main__':
    app.run(debug=True)
