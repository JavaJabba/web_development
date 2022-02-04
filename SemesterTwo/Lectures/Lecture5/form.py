from unicodedata import decimal
from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import InputRequired, NumberRange

class BMIForm(FlaskForm):
    weight = DecimalField("Weight in kg:", validators=[InputRequired(), NumberRange(10, 100)])
    height = DecimalField("Height in metres:", validators=[InputRequired(), NumberRange(0.5, 3)])
    bmi = DecimalField ("BMI:")
    submit = SubmitField("Submit")