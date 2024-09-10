from flask import Flask, render_template_string,jsonify
import random
app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <title>Fruit Bar Machine</title>
      </head>
      <body>
        <h1>Welcome to the Fruit Bar Machine!</h1>
        <div id="fruit-display"></div>
        <script src="static/js/scripts.js"></script>
        <button id="get-fruit-button">Get Random Fruits</button>
      </body>
    </html>
    ''')

@app.route('/get_fruit')
def get_fruit():
    # List of fruit images (you can replace these with actual URLs or local paths)
    fruits = [
        "static/bell.png",
        "static/bell2.png",
        "static/cherry.png",
        "static/cherry2.png",
        "static/organge.png",
        "static/organge2.png",
        "static/organge3.png",
        "static/star.png",
        "static/skull.png"
    ]
    random_fruits = random.sample(fruits, 3)  # Select 3 random fruits
    return jsonify({'fruits': random_fruits})

if __name__ == '__main__':
    app.run(debug=True)