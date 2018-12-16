from datetime import timedelta
from typing import Optional

import bcrypt as bcrypt
from flask import Flask, flash, request, abort, url_for, redirect, render_template, Blueprint
from flask_login import current_user, login_user, login_required, logout_user

from forms.user.login import LoginForm

base = Blueprint("base", __name__)


@base.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        from models.user import User

        user: Optional[User] = User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.checkpw(form.password.data.encode(), user.password):
            from db import db

            user.authenticated = True
            login_user(user)

            db.session.commit()

            next_url = request.args.get("next")

            return redirect(next_url or url_for('index'))

        flash("Email or Password not correct.")
    return render_template('user/login.html', form=form)


@base.route("/logout")
@login_required
def logout():
    from flask_login import current_user
    from models.user import User
    from db import db

    User.query.get(current_user.id).authenticated = False
    logout_user()

    db.session.commit()
    return redirect("/")


@base.route("/register", methods=["GET", "POST"])
def register():
    from forms.user.register import RegisterForm

    form = RegisterForm()

    if form.validate_on_submit():
        from models.user import User
        from db import db

        user = User(email=form.email.data, password=bcrypt.hashpw(form.password.data.encode(), bcrypt.gensalt()))

        db.session.add(user)
        db.session.commit()

        next_url = request.args.get("next")

        return redirect(next_url or url_for('base.login'))
    return render_template('user/register.html', form=form)
