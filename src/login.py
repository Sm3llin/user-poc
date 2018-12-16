from typing import Optional

from flask_login import LoginManager
from werkzeug.exceptions import abort

from models.user import User


login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id: str) -> Optional[User]:
    return User.query.filter_by(email=user_id).first()


@login_manager.unauthorized_handler
def unauthorized():
    # do stuff
    return abort(404)
