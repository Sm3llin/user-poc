from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app
from db import db


migrate = Migrate(app, db, directory="migrations")

manager = Manager(app)
manager.add_command("db", MigrateCommand)

from models.user import User
from models.role import *


if __name__ == "__main__":
    manager.run()
