from typing import Optional

from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required
from sqlalchemy.orm import joinedload

from forms.admin.roles import AssignRoleForm, RoleForm
from models.role import Role
from models.user import User
from util.decorators import role_required

admin = Blueprint("admin", __name__)


@admin.before_request
@login_required
@role_required("admin")
def before_request():
    pass


@admin.route("/")
def index():
    return render_template("admin/index.html")


@admin.route("/users")
def users():
    _users = User.query.options(
        joinedload(User.roles)
    ).all()

    return render_template('admin/users.html', users=_users)


@admin.route("/roles")
def roles():
    return render_template("admin/roles.html")


@admin.route("/role/create", methods=["GET", "POST"])
def create_role():
    form = RoleForm()

    if form.validate_on_submit():
        from db import db

        role = Role(name=form.name.data)

        db.session.add(role)
        db.session.commit()

        return redirect(url_for('admin.create_role'))
    return render_template('admin/create_role.html', form=form)


@admin.route("/role/assign", methods=["GET", "POST"])
def assign_role():
    form = AssignRoleForm()

    if form.validate_on_submit():
        from db import db
        user = form.email.data
        role = form.role.data

        if role not in user.roles:
            user.roles.append(role)

            db.session.commit()

        return redirect(url_for('admin.assign_role'))
    return render_template('admin/assign_role.html', form=form)
