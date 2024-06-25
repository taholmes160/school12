from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    # Correctly import the main blueprint
    from app.main import main as main_blueprint
    from app.users import users as users_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(users_blueprint, url_prefix='/users')

    return app
