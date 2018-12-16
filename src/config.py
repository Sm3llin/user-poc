class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../data/app.db'
    SECRET_KEY = "SHHH! This is a secret!"
