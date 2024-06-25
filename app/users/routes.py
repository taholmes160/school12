from flask import render_template
from app.models import User

def users():
    users = User.query.all()
    return render_template('users/list.html', users=users)
