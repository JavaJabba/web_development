from flask import Flask, render_template
from forms import BandForm
from database import get_db, close_db


app = Flask(__name__)
app.config["SECRET_KEY"] = "SecretKey"
app.teardown_appcontext(close_db)

@app.route("/all_gigs")
def all_gigs():
    db = get_db()
    gigs = db.execute("""SELECT * FROM gigs;""").fetchall()
    return render_template("gigs_html", gigs=gigs, caption="All Gigs!")

@app.route("/future_gigs")
def future_gigs():
    db = get_db()
    gigs = db.execute("""SELECT * FROM gigs,
                            WHERE gig_date >= DATE('now');""").fetchall()
    return render_template("gigs_html", gigs=gigs, caption="Future Gigs!")

@app.route("/future_gigs_by_band", methods=["GET", "POST"])
def future_gigs_by_band():
    form = BandForm()
    gigs = None
    if form.validate_on_submit():
        band = form.bandName.data
        db = get_db()
        gigs = db.execute("""SELECT * FROM gigs, WHERE gig_date >= DATE('now') AND band= ?;""", (band,)).fetchall()
        return render_template("gigs_by_band.html",form=form, gigs=gigs, caption="Get Gigs!!")