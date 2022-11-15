from flask import Flask
from flask import render_template

name = "Jesus Jaime Andrade III"
app = Flask(__name__)

def readDetails(filepath):
    with open(filepath, 'r') as f:
        return [line for line in f]

@app.route("/")

def home():
    name = "Jesus Jaime Andrade III"
    description = readDetails('static/description.txt')
    return render_template("base.html", name=name, aboutMe=description)

@app.route('/user/Jesus')
def user():
    return render_template("user.html")

