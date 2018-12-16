from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms.validators import DataRequired
from wtforms_alchemy import QuerySelectField

from db import ModelForm
from models.role import Role
from models.user import User


class RoleForm(ModelForm):
    class Meta:
        model = Role


class ModifyRoleForm(ModelForm):
    email = QuerySelectField(
        "User",
        query_factory=lambda: User.query.all(),
        get_pk=lambda user: user.id,
        get_label=lambda user: user.email,
        validators=[DataRequired()]
    )
    role = QuerySelectField(
        "Role",
        query_factory=lambda: Role.query.all(),
        get_pk=lambda role: role.id,
        get_label=lambda role: role.name,
        validators=[DataRequired()]
    )
