# app/users/__init__.py
from flask import Blueprint

users = Blueprint('users', __name__)

from . import routes  # Import routes to associate them with the blueprint
