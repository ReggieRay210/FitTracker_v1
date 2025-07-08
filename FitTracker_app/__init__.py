from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__, template_folder='templates',
                static_folder='static',
                instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./fitTracker.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'R2A@16'

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # imports needed for navigation and functionality
    # Collects all the pages from routes.py
    from FitTracker_app.routes import main
    app.register_blueprint(main)

    # retrives user information from the database.
    from FitTracker_app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
