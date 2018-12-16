from functools import wraps

from flask import Blueprint, render_template, redirect, url_for, request, abort
from flask_login import login_required, current_user

admin = Blueprint("admin", __name__)


def role_required(*required_roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if current_user.is_authenticated:
                user_roles = [role.name for role in current_user.roles]

                for role in required_roles:
                    if role not in user_roles:
                        break
                else:
                    return f(*args, **kwargs)
            return abort(404)
        return decorated_function
    return decorator


@admin.before_request
@login_required
@role_required("admin")
def before_request():
    pass


@admin.route("/")
def index():
    return render_template("admin/index.html")


@admin.route("/roles")
def roles():
    return render_template("admin/roles.html")
