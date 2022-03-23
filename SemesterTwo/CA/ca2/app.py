from flask import Flask, render_template, url_for, redirect, session, g, request
from database import close_db, get_db
from flask_session import Session
from forms import LoginForm, RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps


app = Flask(__name__)
app.teardown_appcontext(close_db)
app.config["SECRET_KEY"] = "secret_key"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.before_request
def load_logged_in_user():
    g.user = session.get("player_id", None)

def login_required(view):
    @wraps(view)
    def wrapped_view(**kwrags):
        if g.user is None:
            return redirect(url_for("login", next=request.url))
        return view(**kwrags)
    return wrapped_view

@app.route("/login", methods=["GET", "POST"])
def login():
    form =LoginForm()
    if form.validate_on_submit():
        player_id = form.player_id.data
        password = form.password.data
        db = get_db()
        user_match = db.execute("""SELECT * FROM Players WHERE player_id = ?;""", (player_id,)).fetchone()
        if user_match is None:
            form.player_id.errors.append("Unknown username!")
        elif not check_password_hash(user_match["password"], password):
            form.password.errors.append("Inncorrect Password!")
        else:
            session.clear()
            session["player_id"] = player_id
            return redirect(url_for("index"))
    return render_template("login.html", form=form, title="Login")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        player_id = form.player_id.data
        password = form.password.data
        db = get_db()
        user_check = db.execute("""SELECT * FROM Players WHERE player_id = ?;""", (player_id,)).fetchone()
        if user_check is not None:
            form.player_id.errors.append("Username Taken")
        else:
            db.execute("""INSERT INTO Players (player_id, password) VALUES (?,?);""", (player_id, generate_password_hash(password)))
            db.commit()
            return redirect(url_for("login"))
    return render_template("register.html", form=form, title="Register")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/play", methods=["GET", "POST"])
def play():
    return render_template("play.html")