from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

if os.environ.get('DATABASE_URL') is None:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pokedex.db'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

db = SQLAlchemy(app)

from app import views, models