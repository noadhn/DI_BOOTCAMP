from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('colors_homepage.html')

@app.route('/change_back')
def change_back(color):

    return render_template('change_back.html')


if __name__ == '__main__':
    app.run(debug=True)
