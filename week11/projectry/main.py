from flask import Flask, render_template, url_for, redirect
from datetime import date
import markdown

app = Flask(__name__)
articles = [
    {
        'title': 'Life is beautiful',
        'author': 'Levi Eshkol',
        'date_published': "21.3.21"
    },
    {
        'title': 'Saturday night',
        'author': 'Noa Dahan',
        'date_published': "23.9.21"
    }
]


@app.route("/exercises")
def index():
    ex_file = open("lesson1/exercises.md", "r")
    md_template_string = markdown.markdown(ex_file.read())
    return md_template_string


@app.route("/lesson1")
def lesson1():
    ex_file = open("lesson1/in-this-chapter.md", "r")
    md_template_string = markdown.markdown(ex_file.read())
    return md_template_string


@app.route("/show_date")
def show_date():
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    return "Today is " + d1


@app.route("/blog")
def welcome():
    return render_template('home.html')


@app.route("/portfolio")
def portfolio():
    return render_template('portfolio.html')


@app.route("/blog/articles")
def show_articles():
    return render_template('articles.html', articles=articles)


app.run(debug=True)
