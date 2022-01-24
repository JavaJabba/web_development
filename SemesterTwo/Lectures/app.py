from flask import Flask
from random import choice
from datetime import datetime

app = Flask(__name__)

# @ is a decorator


@app.route("/")
# The route specifies the view function for this endpoint.
def send_greeting():
    return "Hello, World!"


@app.route("/tell_time")
def send_current_date_time():
    return datetime.now().strftime("%H:%M:%S %d-%m-%y")


@app.route("/greet_me")
def send_random_greeting():
    phrases = ["my friend", " There!", ", General Kenobi!"]
    return "Hello" + choice(phrases)


@app.route("/greet_by_name/<name>")
def send_greeting_by_name(name):
    return "Hello, " + name


@app.route("/adios/<name>")
@app.route("/au_revoir/<name>")
def send_parting_by_name(name):
    return "Goodbye, " + name


# @app.errorhandler(404)
# def page_not_found(error):
#     return "Ah, you fucked it!", 404
