from random import choices
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, RadioField
from wtforms.validators import InputRequired, NumberRange


class shiftForm(FlaskForm):
    plainText = StringField("Plain Text:", validators=[InputRequired("This field is required.")])
    shiftNo = IntegerField("Shift:", validators=[NumberRange(1, 25, "Number must be between 1 and 25.")])
    cipherText = StringField("Ciphertext:")
    submit = SubmitField("Submit")

class conversionForm(FlaskForm):
    fromTemp = RadioField("From: ", choices=["Fahrenheit:", "Celsius:", "Kelvin:" ])
    fromNo = IntegerField()
    toTemp = RadioField("To: ", choices=["Fahrenheit:", "Celsius:", "Kelvin:" ])
    result = IntegerField()
    submit = SubmitField("Submit")