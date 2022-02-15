from email.policy import strict
from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.fields import DateField
from wtforms.validators import Input_Required, EqualTo

class BandForm(FlaskForm):
    bandName = StringField("Enter Band Name:", validators=[Input_Required()])
    submit = SubmitField("Submit")

class GigForm(FlaskForm):
    bandName = StringField("Enter Band Name:", validators=[Input_Required()])
    gig_date = DateField("Gig Date:", validators=[Input_Required()])
    submit = SubmitField("Submit")

class RegistrationForm(FlaskForm):
    user_id = StringField("User ID:", validators=[Input_Required()])
    password = PasswordField("Password:", validators=[Input_Required()])
    password2 = PasswordField("Password:", validators=[Input_Required(), EqualTo("password")])
    submit = SubmitField("Submit")