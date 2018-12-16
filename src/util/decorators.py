from functools import wraps
from typing import List, Callable

from flask_login import current_user
from werkzeug.exceptions import abort


def role_required(*required_roles: List[str]) -> Callable:
    """ Control access to views with the `required_roles` as a requirement for the `user` """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # Check auth to ensure that current_user is a sql model
            if current_user.is_authenticated:
                user_roles = [role.name for role in current_user.roles]

                for role in required_roles:
                    if role not in user_roles:
                        # Exit for loop early and avoid the forelse
                        break
                else:
                    return f(*args, **kwargs)
            # 404 as to not show the user a page exists
            return abort(404)
        return decorated_function
    return decorator
