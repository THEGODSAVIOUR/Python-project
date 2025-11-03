from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Retrieve multiple values from the form
        temps = request.form.getlist('temp')
        dews = request.form.getlist('dew')

        # Store results for each pair
        data = []
        for t, d in zip(temps, dews):
            temp = float(t)
            dew = float(d)
            diff = temp - dew

            if diff < 4:
                result = "🌧 High chance of rain!"
                color = "blue"
            elif diff < 8:
                result = "☁️ Possible light rain."
                color = "gray"
            else:
                result = "☀️ No rain expected."
                color = "orange"

            data.append({
                'temp': temp,
                'dew': dew,
                'diff': diff,
                'result': result,
                'color': color
            })

        return render_template('result.html', data=data)

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
