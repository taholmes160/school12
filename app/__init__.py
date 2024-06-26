# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config  # Make sure to import your Config class

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Load the configuration from the Config class
    db.init_app(app)
    # ...
    return app
