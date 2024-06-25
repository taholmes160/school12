from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Initialize the database extension
db = SQLAlchemy()

def create_app(config_class=Config):
    # Create the Flask application
    app = Flask(__name__)
    # Load configurations from the Config class
    app.config.from_object(config_class)

    # Initialize extensions with the app instance
    db.init_app(app)

    # Import blueprints
    from app.main.routes import main as main_blueprint
    from app.users.routes import users as users_blueprint

    # Register blueprints with the application
    app.register_blueprint(main_blueprint)
    app.register_blueprint(users_blueprint, url_prefix='/users')

    return app

