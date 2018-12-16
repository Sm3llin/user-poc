from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import *


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[
        DataRequired(),
        Length(max=32, min=8),
    ])
