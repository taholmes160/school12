# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    # Import and register the main blueprint
    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Add other blueprints or configurations as needed

    return app
