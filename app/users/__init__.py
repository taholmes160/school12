from flask import Blueprint

# Create a Blueprint for the 'users' part of your application.
users = Blueprint('users', __name__)

# Import the routes to associate them with the blueprint.
from . import routes
