from flask import Flask, render_template, url_for, flash, redirect, request
from flask_blog import app, db, bcrypt
from flask_blog.forms import RegisterationForm, LoginForm
from flask_blog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


posts = [
    {
        "name": "Yasir Khan",
        "title" : "Blog Post 1",
        "content" : "First content post",
        "date_posted" : "3 October, 2022"
    },
    {
        "name": "Zubair Sajjad",
        "title" : "Blog Post 2",
        "content" : "Second content post",
        "date_posted" : "4 October, 2022"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def aboutPage():
    return render_template("about.html", title="About")


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can now able to Login.', 'success')
        return redirect(url_for('login'))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
        
    form = LoginForm()
    if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                next_page = request.args.get("next")
                return redirect(next_page) if next_page else  redirect(url_for('home'))
            else:
                flash("Login Unsuccessful! Please Check email and Password", "danger")

    return render_template("login.html", title="login", form=form)    



@app.route("/logout")
def logout():
    logout_user()



@app.route("/account")
@login_required
def account():
    return render_template("account.html", title="Account")