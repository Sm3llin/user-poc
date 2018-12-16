class Config:
    SECRET_KEY = "SHHH! This is a secret!"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../data/app.db'
    SQLALCHEMY_ECHO = True
