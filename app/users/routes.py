from flask import render_template, Blueprint
from app.models import User  # Import the User model from the models module

users = Blueprint('users', __name__, url_prefix='/users')

@users.route('/list')
def list_users():
    # Fetch the users from the database using the User model
    users = User.query.all()
    return render_template('users/list.html', users=users)

