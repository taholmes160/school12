from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config
from app.main.routes import home
from app.users.routes import users

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    # Create SQLAlchemy engine and session
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    Session = sessionmaker(bind=engine)
    app.db_session = Session()

    # Register routes
    app.add_url_rule('/', 'home', home)
    app.add_url_rule('/users', 'users', users)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        app.db_session.close()
        return app

    return app
