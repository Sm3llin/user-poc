from typing import Optional

from wtforms import PasswordField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError

from db import ModelForm
from models.user import User


class RegisterForm(ModelForm):
    class Meta:
        model = User

    password = PasswordField(validators=[
        DataRequired(),
        Length(max=32, min=8),
        EqualTo("confirm", "Both passwords must match")
    ])
    confirm = PasswordField("Repeat password")

    def validate_email(self, field):
        user: Optional[User] = User.query.get(field.data)

        if user:
            raise ValidationError("Email already in use.")
