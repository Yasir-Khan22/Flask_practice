from distutils.log import debug
from turtle import title
from flask import Flask, render_template, url_for

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)