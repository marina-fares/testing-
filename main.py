from flask import Flask, render_template, request, session 

from flask_session import Session 

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

notes=[]

@app.route('/')
def hello_world():
    return render_template('main.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route("/", methods=["GET", "POST"])
def hello():
    if session.get("notes") is None:
        session["notes"] = []
    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)
    return render_template("hello.html", notes=session["notes"])