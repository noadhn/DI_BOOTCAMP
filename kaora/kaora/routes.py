from flask import render_template, url_for, flash, redirect
from kaora.forms import RegistrationForm, LoginForm
from kaora import app
from kaora.models import User, Product, Post


@app.route("/")
def index():
    return render_template("index.html", title="Homepage")


@app.route("/gallery")
def gallery():
    return render_template("gallery_by_collections.html", title="gallery")


@app.route("/all_products")
def products():
    return render_template("gallery_all.html", title="gallery")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Nice to meet you {form.username.data}!", 'info')
        return redirect(url_for('index'))
    return render_template("register.html", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@noa.com' and form.password.data == 'password':
            flash(f"Your'e in!", 'info')
            return redirect(url_for('home'))
        else:
            flash(f"Log in was unsuccessful", 'danger')
            return redirect(url_for('login'))
    return render_template('login.html', form=form)
