from flask import Flask, render_template, url_for
from forms import RegisterationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dde3df9f7f1c88768cf8736c6af3f3'


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


@app.route("/register")
def register():
    form = RegisterationForm()
    return render_template("register.html", title="Register", form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="login", form=form)



if __name__ == '__main__':
    app.run(debug=True)