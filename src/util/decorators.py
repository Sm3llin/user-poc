from functools import wraps

from flask_login import current_user
from werkzeug.exceptions import abort


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
