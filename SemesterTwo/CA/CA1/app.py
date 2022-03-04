from tabnanny import check
from flask import Flask, render_template, url_for, redirect, session, g, request
from database import close_db, get_db
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegisterForm, LoginForm
from functools import wraps

'''

'''

app = Flask(__name__)
app.teardown_appcontext(close_db)
app.config["SECRET_KEY"] = "secret_key"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.before_request
def load_logged_in_user():
    g.user = session.get("user_id", None)

def login_required(view):
    @wraps(view)
    def wrapped_view(**kwrags):
        if g.user is None:
            return redirect(url_for("login", next=request.url))
        return view(**kwrags)
    return wrapped_view

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        player_id = form.player_id.data
        password = form.password.data
        password2 = form.password2.data
        game = form.games.data
        faction = form.factions.data
        db = get_db()
        user_check = db.execute("""SELECT * FROM Players WHERE player_id = ?;""", (player_id,)).fetchone()
        if user_check is not None:
            form.player_id.errors.append("Username Taken")
        else:
            db.execute("""INSERT INTO Players (player_id, password) VALUES (?,?);""", (player_id, generate_password_hash(password)))
            db.execute("""INSERT INTO PlayerGameRelation VALUES (?,?)""", (player_id, game))
            db.commit()
            return redirect(url_for("login"))
        return render_template("register.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = RegisterForm()
    if form.validate_on_submit():
        player_id = form.player_id.data
        password = form.password.data
        db = get_db()
        user_match = db.execute("""SELECT * FROM Players WHERE player_id = ?;""", (player_id,)).fetchone()
        if user_match is not None:
            form.player_id.errors.append("Unknown username!")
        elif not check_password_hash(user_match["password"], password):
            form.password.errors.append("Inncorrect Password!")
        else:
            session.clear()
            session["player_id"] = player_id
            return redirect(url_for("index"))
        return render_template("login.html", form=form)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

@app.route("/", methods=["GET", "POST"])
def index():
    '''
    if user in session
        display query options and shop route
        link to account 
    else 
        display login
    '''
    return render_template("index.html")



@app.route("/account", methods=["GET","POST"])
def account():

    '''
    various user details with selectfields that can be changed.

    adding new games and factions to your account

    possible change password??
    '''
