from flask import render_template
from . import main  # Import the blueprint

@main.route('/')
def home():
    # Render the 'home.html' template located under 'templates/main/'
    return render_template('main/home.html')

    