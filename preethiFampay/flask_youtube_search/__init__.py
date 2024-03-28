from flask import Flask
from .routes import main
from .database import db

def create_app(config_file='settings.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    db.init_app(app)
    app.register_blueprint(main)
    return app
