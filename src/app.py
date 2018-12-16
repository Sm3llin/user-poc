from flask import Flask, render_template, redirect
from flask_login import login_required, current_user

from blueprints.admin import admin
from blueprints.base import base
from blueprints.exceptions import exc

from login import login_manager
from db import db

app = Flask(__name__)
app.config.from_object("config.Config")


db.init_app(app)
login_manager.init_app(app)

app.register_blueprint(exc)
app.register_blueprint(base, url_prefix="/")
app.register_blueprint(admin, url_prefix="/admin")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/secure")
@login_required
def secure():
    return render_template("secure.html")


@app.route("/make_me_admin")
@login_required
def admin_maker():
    from models.role import Role

    admin_role = Role.query.filter_by(name="admin").first()

    if not admin_role:
        admin_role = Role(name="admin")
        db.session.add(admin_role)

    if "admin" not in current_user.roles:
        current_user.roles = [admin_role]

    db.session.commit()

    return redirect("/admin")


if __name__ == '__main__':
    app.run(debug=True)
