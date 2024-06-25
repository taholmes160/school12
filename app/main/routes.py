from flask import current_app

def home():
    template = current_app.jinja_env.get_template('main/home.html')
    return template.render()
