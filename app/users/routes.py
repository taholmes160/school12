from flask import Blueprint, render_template
from app.models import User

users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.route('/list')
def list_users():
    """
    Render the list of users.
    """
    users = User.query.all()
    return render_template('users/list.html', users=users)


