from flask_login import UserMixin

from db import db
from models.role import *


class User(db.Model, UserMixin):
    """An admin user capable of viewing reports.

    :param str email: email address of user
    :param str password: encrypted password for the user

    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(255), nullable=True, unique=True)
    password = db.Column(db.String(255), nullable=False)
    authenticated = db.Column(db.Boolean, default=False)

    # Define the relationship to Role via UserRoles
    roles = db.relationship('Role', secondary='user_roles')

    def __repr__(self):
        return f'<User email={self.email}>'

    def has_role(self, role: str) -> bool:
        return role in [r.name for r in self.roles]

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False
