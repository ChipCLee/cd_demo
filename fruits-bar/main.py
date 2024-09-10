from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

symbols = ["Cherry", "Bell", "Lemon", "Orange", "Star", "Skull"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/spin')
def spin():
    rolled_symbols = random.choices(symbols, k=3)
    return jsonify(rolled_symbols)

if __name__ == '__main__':
    app.run(debug=True)
