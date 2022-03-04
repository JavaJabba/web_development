from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField
from wtforms.validators import InputRequired, EqualTo

class LoginForm(FlaskForm):
    player_id = StringField("Username:", validators=[InputRequired()])
    password = PasswordField("Password:", validators=[InputRequired()])
    submit = SubmitField("Submit")

class RegisterForm(FlaskForm):
    player_id = StringField("Username:", validators=[InputRequired()])
    password = PasswordField("Password:", validators=[InputRequired()])
    password2 = PasswordField("Repeat password:", validators=[InputRequired(), EqualTo("password")])
    games = RadioField("What games do you play?", validators=[InputRequired()], choices="""SELECT * FROM games;""")
    factions = RadioField("What factions do you play?", validators=[InputRequired()], choices="""SELECT * FROM factions;""")
    submit = SubmitField("Submit")