from asyncio.windows_events import NULL
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/spy", methods=["GET", "POST"])
def spy_intro():
    if request.method == "GET":
        return render_template("spyform.html")
    else:
        given_name = request.form["given_name"]
        family_name = request.form["family_name"]
        return render_template("spyresponse.html", given_name=given_name, family_name=family_name)

@app.route("/morse", methods=["GET", "POST"])
def morse():
    if request.method == "GET":
        return render_template("morse_form.html")
    else:
        message = request.form["message"]
        cleaned_message = message.strip().upper()
        morse = ""
        morse_dict = {"A":".-", "B":"-...", "C":"-.-.", " ":"/"}
        if message == "":
            error = "Text Box is blank! Please try again!"
            return render_template("morse_form.html", error=error)
        for char in cleaned_message:
            if char not in morse_dict:
                error = "Invalid Character entered, please try again!"
                return render_template("morse_form.html", error=error)
            else:
                code = morse_dict[char]
                morse = morse + code + " "
        return render_template("morse_response.html", message=message, morse=morse)

@app.route("/lengths", methods=["GET", "POST"])
def lengths():
    if request.method == "GET":
        return render_template("lengthform.html")
    else:
        inches = request.form["inches"]
        centimetres = request.form["centimetres"]
        if inches == "" and centimetres == "":
            error = "Please fill in at least one field!"
            return render_template("lengthform.html", error=error)
        elif inches != "" and centimetres != "":
            error = "Please fill in ONLY one field!"
            return render_template("lengthform.html", error=error)
        elif inches != NULL and centimetres == "":
            inches = float(inches)
            centimetres = inches * 2.54
            return render_template("lengthform.html", inches=inches, centimetres=centimetres)
        elif centimetres !=NULL and inches == "":
            centimetres = float(centimetres)
            inches = centimetres / 2.54
            return render_template("lengthform.html", inches=inches, centimetres=centimetres)

@app.route("/spy_name")
def spyname():
    firstPart = {"A":"Golden", "B":"Red", "C":"Rogue", "D":"Alpha", "E":"Iron", "F":"Secret", "G":"Hot", "H":"Green", "I":"Hugh", "J":"Wild", "K":"Silver", "L":"Slick", "M":"Big", "N":"Deadly", "O":"Flash", "P":"Black", "Q":"Cold", "R":"Wild", "S":"Dark", "T":"Blue", "U":"Stone", "V":"Lone", "W":"Sly", "X":"Sterling", "Y":"Ultimate", "Z":"Rocket"}
    secondPart = ["Danger", "Spider", "Lightning", "Ghost", "Ninja", "Wolf", "Storm", "Scorpion", "Cobra", "Shadow", "Jaguar", "Jeegoh"]