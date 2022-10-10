from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegisterationForm, LoginForm
# from email.policy import default
# from enum import unique
# from operator import truediv
# from turtle import title

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dde3df9f7f1c88768cf8736c6af3f3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}, {self.password}, {self.image_file}')"



class Post(db.Model):
    id = db.Column(db.integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.Datetime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Test, nullable=False)

    def __repr__(self):
        return f"User('{self.title}, {self.date_posted}')"


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
    form = RegisterationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash('You have been logged In!', 'success')
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful! Please Check Username and Password", "danger")

    return render_template("login.html", title="login", form=form)



if __name__ == '__main__':
    app.run(debug=True)