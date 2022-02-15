from sqlite3 import IntegrityError
from flask import Flask, render_template
from forms import BandForm, GigForm, RegistrationForm
from datetime import datetime
from database import get_db, close_db
from werkzeug.security import generate_password_hash

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

@app.route("/insert_gig", methods=["GET", "POST"])
def insert_gig():
    form = GigForm()
    message = ""
    if form.validate_on_submit():
        band = form.bandName.data
        gig_date = form.gig_date.data
        if gig_date <= datetime.now().date():
            form.gig_date.errors.append("Date must be in the future")
        else:
            db = get_db()
            conflicting_gig = db.execute("""SELECT * FROM gigs, WHERE gig_date = ?""", (gig_date,)).fetchone()
            if conflicting_gig is not None:
                form.gig_date.errors.append("Gig clashes with another!")
            db.execute("""INSERT INTO gigs (band, gig_date), VALUES (?, ?)""", (band, gig_date))
            db.commit()
            message = "New Gig successfully inserted"
    return render_template("insert_gig.html", form=form, message=message)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user_id = form.user_id.data
        password = form.password.data
        password2 = form.password2.data
        db = get_db()
        try:
            db.execute("""INSERT INTO users (user_id, password), VALUES (?, ?)""", (user_id, generate_password_hash(password)))
            db.commit()
            return "Redirect to login"
        except IntegrityError:
            form.user_id.errors.append("User ID is already taken!")
    return render_template("register.html", form=form)