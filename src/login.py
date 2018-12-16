from typing import Optional

from flask_login import LoginManager
from sqlalchemy.orm import joinedload
from werkzeug.exceptions import abort

from models.user import User


login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id: str) -> Optional[User]:
    # joinedload roles as to avoid multiple queries for role checking
    return User.query.filter_by(email=user_id).options(
        joinedload(User.roles)
    ).first()


@login_manager.unauthorized_handler
def unauthorized():
    # do stuff
    return abort(404)
