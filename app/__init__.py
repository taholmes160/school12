from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__, template_folder='app/templates')
    app.config.from_object(config_class)

    print(f"Template folder: {app.template_folder}")

    db.init_app(app)

    # Create SQLAlchemy engine and session
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    Session = sessionmaker(bind=engine)
    app.db_session = Session()

    # Register routes
    from .main.routes import home
    from .users.routes import users
    app.add_url_rule('/', 'home', home)
    app.add_url_rule('/users', 'users', users)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        app.db_session.close()
        return app

    return app
