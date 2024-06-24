from flask import render_template, current_app
from app.users import bp
from app.models import User

@bp.route('/users')
def list_users():
    users = current_app.db_session.query(User).all()
    return render_template('users/list.html', users=users)