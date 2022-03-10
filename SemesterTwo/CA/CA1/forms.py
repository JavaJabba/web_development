from datetime import date
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectMultipleField, DateField
from wtforms.validators import InputRequired, EqualTo

class LoginForm(FlaskForm):
    player_id = StringField("Username:", validators=[InputRequired()])
    password = PasswordField("Password:", validators=[InputRequired()])
    submit = SubmitField("Submit")

class RegisterForm(FlaskForm):
    player_id = StringField("Username:", validators=[InputRequired()])
    password = PasswordField("Password:", validators=[InputRequired()])
    password2 = PasswordField("Repeat password:", validators=[InputRequired(), EqualTo("password")])
    first_name = StringField("First name:", validators=[InputRequired()])
    last_name = StringField("last name:", validators=[InputRequired()])
    games = SelectMultipleField("What games do you play?", validate_choice=False ,validators=[InputRequired()], choices=["Warhammer: Age of Sigmar", "Warhammer: 40'000", "Bolt Action", "Marvel Crisis Protocol", "Gaslands", "Silver Bayonet"])
    factions = SelectMultipleField("What factions do you play?", validate_choice=False , validators=[InputRequired()], choices=["German", "Japanese", "French", "British", "Soviet Union", "Italian", "Space Marines", "Orks", "World Eaters", "Daemons", "Imperial Guard", "Sisters of Battle", "Drukari", "Orruk Warclans", "Orge Mawclans", "Stormcast Eternals", "Idoneth Deepkin", "Blades of Khorne", "Maggotkin of Nurgle", "Slaves to Darkness", "Lumineth Realmlords", "Tau", "Adeptus Mechanicus"])
    date_joined = DateField("What date did you join?")
    submit = SubmitField("Submit")