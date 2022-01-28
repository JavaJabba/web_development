from pipes import Template
from re import template
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/greet_by_name/<name>")
def send_greeting_by_name(name):
    return render_template("greet1.html", name=name)

#Jinja2 Template - Html with placeholders.

@app.route("/greet_across_the_world/<language>")
def send_greeting_in_language(language):
    hello_dict = {"en":"Hello", "fr":"Bonjour", "es":"Hola"}
    greeting = hello_dict.get(language, "Hi")
    return render_template("greet2.html", greeting = greeting)

@app.route("/au_revoir/<name>")
@app.route("/adios/<name>")
@app.route("/ciao")
def send_parting_by_name(name=None):
    return render_template("bye.html", name=name)