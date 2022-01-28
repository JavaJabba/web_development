from flask import Flask, render_template, request


app = Flask(__name__)

# @app.route("/form")
# def send_form():
#     return render_template("form.html")

# @app.route("/response", methods=["POST"])
# def send_response():
#     first_name = request.form["first_name"]
#     last_name = request.form["last_name"]
#     return render_template("response.html", first_name=first_name, last_name=last_name)

@app.route("/greet_me", methods=["GET", "POST"])
def send_greeting():
    if request.method == "GET":
        return render_template("form.html")
    else:
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        return render_template("response.html", first_name=first_name, last_name=last_name)