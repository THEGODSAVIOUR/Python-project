from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import numpy as np

# --- Initialize Flask app ---
app = Flask(__name__)
CORS(app)  # Allow frontend (JS) to talk to Flask

# --- Routes ---
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.json.get('rainfall', [])
        algorithm = request.json.get('algorithm', 'bubble')

        if not data:
            return jsonify({'error': 'No rainfall data provided'}), 400

        # --- Sorting algorithms ---
        if algorithm == 'bubble':
            sorted_data = bubble_sort(data)
        elif algorithm == 'selection':
            sorted_data = selection_sort(data)
        elif algorithm == 'insertion':
            sorted_data = insertion_sort(data)
        elif algorithm == 'quick':
            sorted_data = quick_sort(data)
        else:
            sorted_data = bubble_sort(data)  # Default fallback

        # --- Calculations ---
        avg = np.mean(sorted_data)
        predicted = avg * 1.1  # Simple example: +10% trend prediction

        # --- Response ---
        return jsonify({
            'original': data,
            'sorted_data': sorted_data,
            'average': round(float(avg), 2),
            'prediction': round(float(predicted), 2)
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# --- Sorting Algorithms ---

def bubble_sort(arr):
    a = arr[:]
    for i in range(len(a)):
        for j in range(0, len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def selection_sort(arr):
    a = arr[:]
    for i in range(len(a)):
        min_idx = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


def insertion_sort(arr):
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)


# --- Run Server ---
if __name__ == '__main__':
    app.run(debug=True)
