from flask import Flask, render_template
from forms import shiftForm, conversionForm




app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key"

@app.route("/shift", methods=["GET", "POST"])
def shiftCipher():
    form = shiftForm()
    cipherText = ""
    if form.validate_on_submit():
        shiftNo = form.shiftNo.data
        plainText = form.plainText.data
        for char in plainText:
            if char.isupper():
                cipherText += chr((ord(char) - 65 + shiftNo) % 26 + 65)
            elif char.islower():
                cipherText += chr((ord(char) - 97 + shiftNo) % 26 + 97)
            else:
                cipherText += char
        form.cipherText.data = cipherText
    return render_template("shift_form.html", title="Caeser Shift Cipher", cipherText=cipherText, form=form )

@app.route("/conversion", methods=["GET", "POST"])
def conversion():
    form = conversionForm()
    if form.validate_on_submit:
        fromTemp = form.fromTemp.data
        fromNo = form.fromNo.data
        toTemp = form.toTemp.data
        if fromTemp == "Celsius" and toTemp == "Fahrenheit":
            result = 9/5 * fromNo + 32
            form.result.data = result
        elif fromTemp == "Kelvin" and toTemp == "Fahrenheit":
            result = 9/5 * (fromNo - 273) + 32
            form.result.data = result
        elif fromTemp == "Fahrenheit" and toTemp == "Celsius":
            result = 5/9 * (fromNo - 32)
            form.result.data = result
        elif fromTemp == "Celsius" and toTemp == "Kelvin":
            result = fromNo + 273
            form.result.data = result
        elif fromTemp == "Kelvin" and toTemp == "Celsius":
            result = fromNo - 273
            form.result.data = result
        elif fromTemp == "Fahrenheit" and toTemp == "Kelvin":
            result = 5/9 * (fromNo - 32) + 273
            form.result.data = result
    return render_template("conversion_form.html", title="Temperature Conversion", form=form)