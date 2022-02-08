from flask import Flask, render_template
from form import AliveForm, ToppingForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key"
@app.route("/alive", methods=["GET", "POST"])
def alive():
    form = AliveForm()
    outcome = ""
    if form.validate_on_submit():
        alive = form.alive.data
        if alive == True:
            outcome = "False, He's been dead for a long time!"
        else:
            outcome = "Correct!"
    return render_template("alive_form.html", title="Elvis Lives?" ,form=form, outcome=outcome)

@app.route("/topping", methods=["GET", "POST"])
def topping():
    form = ToppingForm()
    outcome = ""
    if form.validate_on_submit():
        topping = form.topping.data
        if topping == "Anchovies":
            outcome = "Correct!"
        else:
            outcome = "You are wrong!"
    return render_template("toppingform.html", title="Elvis Eats?" ,form=form, outcome=outcome)