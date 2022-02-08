from xmlrpc.client import boolean
from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField, SelectField
from wtforms.validators import InputRequired

class AliveForm(FlaskForm):
    alive = BooleanField("Check the box if you think Elvis is still alive:")
    submit = SubmitField("Submit") 

class ToppingForm(FlaskForm):
    topping = SelectField("Which topping do you think Elvis prefers?", 
        choices=["Anchovies", "Chocolate", "Morphine", "Pepperoni", "Pineapple"] ,validators=[InputRequired()])
    submit = SubmitField("Submit")
