from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        temps = request.form.getlist('temp')
        dews = request.form.getlist('dew')
        data = []

        for temp, dew in zip(temps, dews):
            temp = float(temp)
            dew = float(dew)

            # Formula calculations
            specific_humidity = 6.11 * (10 ** ((7.5 * dew) / (237.3 + dew)))
            saturation_point = 6.11 * (10 ** ((7.5 * temp) / (237.3 + temp)))
            relative_humidity = (specific_humidity / saturation_point) * 100

            data.append({
                'temp': temp,
                'dew': dew,
                'rh': relative_humidity
            })

        # Sort based on relative humidity
        data.sort(key=lambda x: x['rh'])

        # Find highest relative humidity
        highest = max(data, key=lambda x: x['rh'])

        # Determine rainfall prediction
        if highest['rh'] > 80 and highest['temp'] < 25:
            prediction = "High chance of rainfall 🌧"
        else:
            prediction = "Low chance of rainfall ☀️"

        return render_template('result.html', data=data, highest=highest, prediction=prediction)

    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
