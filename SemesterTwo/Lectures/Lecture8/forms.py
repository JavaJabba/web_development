from email.policy import strict
from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Input_Required

class BandForm(FlaskForm):
    bandName = StringField("Enter Band Name:", validators=Input_Required)
    submit = SubmitField("Submit")