# Used to communicate with the __init__.py file for flask application setup.
# This file is the entry point for running the Flask application.
# It imports the create_app function from the FitTracker_app package and
# runs the application.

from FitTracker_app import create_app

flask_app = create_app()

if __name__ == '__main__':
    flask_app.run(debug=True)
