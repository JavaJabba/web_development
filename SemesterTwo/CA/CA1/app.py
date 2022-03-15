from flask import Flask, render_template, url_for, redirect, session, g, request
from database import close_db, get_db
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegisterForm, LoginForm, FindPlayersForm, AddGames
from functools import wraps

'''
Function of this program is to create users based on members of the club and have information stored about when they joined, 
what games they play and what factions within those games they play. A User can log on, search to see how many players play a given faction 
or game as well as go to their account details and add new games or factions they have picked up.

More functionality was planned such as a admin user, the ability for a user to also delete a game or faction from their account, the ability
for the admin to add more games and faction choices but alas, I ran out of time.
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
        game = form.games.data
        faction = form.factions.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        date_joined = form.date_joined.data
        db = get_db()
        user_check = db.execute("""SELECT * FROM Players WHERE player_id = ?;""", (player_id,)).fetchone()
        if user_check is not None:
            form.player_id.errors.append("Username Taken")
        else:
            db.execute("""INSERT INTO Players (player_id, password, first_name, last_name, date_joined) VALUES (?,?,?,?,?);""", (player_id, generate_password_hash(password), first_name, last_name, date_joined))
            db.execute("""INSERT INTO PlayerGameRelation (player_id, game_name) VALUES (?,?);""", (player_id, game))
            db.execute("""INSERT INTO PlayerFactionRelation (player_id, faction_name) VALUES (?,?);""", (player_id, faction))
            db.commit()
            return redirect(url_for("login"))
    return render_template("register.html", form=form, title="Register")

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

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html", title="Home")

@app.route("/findplayers", methods=["GET","POST"])
def findplayers():
    form = FindPlayersForm()
    if "player_id" not in session:
        return redirect(url_for("login"))
    elif form.validate_on_submit():
        game_name = form.games.data
        faction_name = form.factions.data
        db = get_db()
        game_query = db.execute(""" SELECT COUNT(player_id) FROM PlayerGameRelation WHERE game_name = ?;""", (game_name,)).fetchone()
        faction_query = db.execute(""" SELECT COUNT(player_id) FROM PlayerFactionRelation WHERE faction_name = ?; """, (faction_name,)).fetchone()
        session["game_name"] = game_name
        session["faction_name"] = faction_name
        session["game_query"] = game_query
        session["faction_query"] = faction_query
    return render_template("findplayers.html", form=form, title="Find Players!")


@app.route("/account", methods=["GET","POST"])
def account():
    form = AddGames()
    if "player_id" not in session:
        return redirect(url_for("login"))
    elif form.validate_on_submit():
        game_name = form.games.data
        faction_name = form.factions.data
        db = get_db()
        db.execute("""INSERT INTO PlayerGameRelation (player_id, game_name) VALUES (?,?)""", (session["player_id"], game_name))
        db.execute("""INSERT INTO PlayerFactionRelation (player_id, faction_name) VALUES (?,?)""", (session["player_id"], faction_name))
        message = "Game Added"
    return render_template("account.html", form=form, title="Account")


