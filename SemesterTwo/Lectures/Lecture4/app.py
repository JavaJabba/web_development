from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/morse", methods=["GET", "POST"])
def morse():
    if request.method == "GET":
        return render_template("morse_form.html")
    else:
        message = request.form("message")
        cleaned_message = message.strip().upper()
        morse = ""
        morse_dict = {"A":".-", "B":"-...", "C":"-.-.", " ":"/"}
        for char in cleaned_message:
            code = morse_dict[char]
            morse = morse + code + " "
        return render_template("morse_response.html", message=message, morse=morse)

@app.route("/bmi", methods=["GET", "POST"])
def bmi():
    if request.method == "GET":
        return render_template("bmi_form.html", bmi="", weight="", height="")
    else:
        weight = request.form("weight")
        height = request.form("height")
        weight = float(weight)
        height = float(height)
        bmi = weight / (height * height)
        return render_template("bmi_form.html", bmi=bmi, weight=weight, height=height)

