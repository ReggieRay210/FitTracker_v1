from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__, template_folder='templates',
                static_folder='static',
                instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fitTracker.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'R2A@16'

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        # imports needed for navigation and functionality
        # Collects all the pages from routes.py and database information from models.py
        from FitTracker_app import models, routes
        db.create_all()
    return app
