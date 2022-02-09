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
            return render_template("morse_form.html", error="Text Box is blank! Please try again!")
        for char in cleaned_message:
            if char not in morse_dict:
                return render_template("morse_form.html", error="Invalid Character entered, please try again!")
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
            return render_template("lengthform.html", error="Please fill in at least one field!")
        elif inches != "" and centimetres != "":
            return render_template("lengthform.html", error="Please fill in ONLY one field!")
        elif inches != NULL and centimetres == "":
            inches = float(inches)
            centimetres = inches * 2.54
            return render_template("lengthform.html", inches=inches, centimetres=centimetres)
        elif centimetres !=NULL and inches == "":
            centimetres = float(centimetres)
            inches = centimetres / 2.54
            return render_template("lengthform.html", inches=inches, centimetres=centimetres)

@app.route("/spy_name", methods=["GET", "POST"])
def spyname():
    firstPart = {"A":"Golden", "B":"Red", "C":"Rogue", "D":"Alpha", "E":"Iron", "F":"Secret", "G":"Hot", "H":"Green", "I":"Hugh", "J":"Wild", "K":"Silver", "L":"Slick", "M":"Big", "N":"Deadly", "O":"Flash", "P":"Black", "Q":"Cold", "R":"Wild", "S":"Dark", "T":"Blue", "U":"Stone", "V":"Lone", "W":"Sly", "X":"Sterling", "Y":"Ultimate", "Z":"Rocket"}
    secondPart = {"01":"Danger", "02":"Spider", "03":"Lightning", "04":"Ghost", "05":"Ninja", "06":"Wolf", "07":"Storm", "08":"Scorpion", "09":"Cobra", "10":"Shadow", "11":"Jaguar", "12":"Jeegoh"}
    if request.method == "GET":
        return render_template("spyname.html")
    else:
        givenName = request.form["given_name"]
        dob = request.form["dob"]
        spyFirst = firstPart[givenName[0]]
        spySecond = secondPart[dob[5:7]]
        spyname = "Your Spy name is " + spyFirst + " " + spySecond
        return render_template("spyname.html", givenName=givenName, dob=dob, spyname=spyname)

