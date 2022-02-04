from unicodedata import decimal
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import InputRequired

class BMIForm(FlaskForm):
    weight = DecimalField("Weight in kg:", validators=[InputRequired])
    height = DecimalField("Height in metres:", validators=[InputRequired])
    bmi = DecimalField ("BMI:")
    submit = SubmitField("Submit")