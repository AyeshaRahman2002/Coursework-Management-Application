import os

WTF_CSRF_ENABLED = True

SECRET_KEY = 'Kumhrauli@345'

SQLALCHEMY_TRACK_MODIFICATIONS = True 

basedir = os.path.abspath(os.path.dirname(__file__))   #to figure out the path directory

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')