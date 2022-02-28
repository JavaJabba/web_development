from flask import Flask, request, render_template, session
from forms import numberForm
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/guess", methods=["GET", "POST"])
def guessNumber():
    form = numberForm()
    userNumber = form.userNumber.data
    if "friendNumber" not in session:
        session["friendNumber"] = False    



