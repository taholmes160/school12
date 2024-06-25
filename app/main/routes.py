from flask import current_app, render_template

def home():
    return render_template('app/main/templates/main/home.html')

