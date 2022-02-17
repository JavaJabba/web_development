from flask import Flask, render_template
from database import get_db, close_db
from forms import WinnersForm, minWinnersForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key"
app.teardown_appcontext(close_db)

@app.route("/winners", methods=["GET", "POST"])
def getWinners():
    form = WinnersForm()
    country = form.country.data
    winners = ""
    if form.validate_on_submit():
        db = get_db()
        winners = db.execute(""" SELECT * FROM winners WHERE country = ?""", (country,)).fetchall()
        if winners == []:
            form.country.errors.append("This country either never won or never participated, please try again!")
    return render_template("winners.html", form=form, winners=winners, caption="Eurovision Winners")


@app.route("/min_winners", methods=["GET", "POST"])
def getMinWinners():
    form = minWinnersForm()
    country = form.country.data
    points = form.points.data
    winners = ""
    if form.validate_on_submit():
        db = get_db()
        if country != None:
            winners = db.execute(""" SELECT * FROM winners WHERE country = ?""", (country,)).fetchall()
        elif points != "":
            winners = db.execute(""" SELECT * FROM winners WHERE points >= ?;""", (points,)).fetchall()
        elif country == "" and points == "":
            winners = db.execute(""" SELECT * FROM winners WHERE country = ? AND points >= ?; """, (country, points)).fetchall()
        else:
            winners = db.execute(""" SELECT * FROM winners """)
    return render_template("min_winners.html", form=form, winners=winners, caption="Eurovision Winners")