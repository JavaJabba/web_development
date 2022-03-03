from random import randint
from flask import Flask, request, render_template, session
from forms import numberForm
from flask_session import Session

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/guess", methods=["GET", "POST"])
def guess():
    form = numberForm()
    userNumber = form.userNumber.data
    if request.method == "GET":
        if "secretNumber" not in session:
            session["secretNumber"] = randint(1, 100)
            return render_template("number.html", form=form, secretNumber=session["secretNumber"], userNumber=userNumber)
    if userNumber == session["secretNumber"]:
        message = "You've guessed it!"
    else:
        message = "You've guessed wrong!"
    return render_template("number.html", form=form, secretNumber=session["secretNumber"], userNumber=userNumber, message=message)
        
        
             

