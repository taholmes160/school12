# app/routes.py

from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from app.models import User
from app import app

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('dashboard'))  # Redirect to dashboard or desired page after login
        else:
            error = 'Invalid username or password. Please try again.'
            return render_template('login.html', error=error)
    
    return render_template('login.html')

# Logout route
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))  # Redirect to the homepage or desired page after logout
