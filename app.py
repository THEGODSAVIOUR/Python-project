from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        temp = float(request.form['temperature'])
        dew = float(request.form['dew_point'])
    except ValueError:
        return render_template('result.html',
                               result="⚠️ Invalid input",
                               color_class="red-text",
                               temp="N/A", dew="N/A", diff="N/A")

    diff = temp - dew

    if diff <= 4:
        result = "🌧️ High chance of rainfall!"
        color_class = "blue-text"
    else:
        result = "☀️ Low chance of rainfall."
        color_class = "red-text"

    return render_template('result.html',
                           result=result,
                           color_class=color_class,
                           temp=temp,
                           dew=dew,
                           diff=diff)


if __name__ == '__main__':
    app.run(debug=True)
