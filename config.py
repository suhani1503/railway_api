import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_random_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://user:password@localhost/railway_db'
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'jwt_secret_key'
