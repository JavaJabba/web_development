from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField

class numberForm(FlaskForm):
    userNumber = IntegerField("Guess the Number!")
    submit = SubmitField("Submit")