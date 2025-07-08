from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from FitTracker_app.forms import registrationForm, loginForm
from FitTracker_app.models import User
from FitTracker_app import db
# This file defines the routes for the FitTracker pages that is listed in the
# templates folder.

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/register', methods=['GET', 'POST'])
def register():
    form = registrationForm()
    if form.validate_on_submit():
        # check if account exists
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash('Account already exists. Please Login.', 'warning')
            return redirect(url_for('main.login'))

        # Create a new user
        user = User()

        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        # Redirect to login page after registration
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            # Log the user in
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('main.dashboard'))
        else:
            flash('Invalid email or password. Please try again.', 'danger')
    return render_template('login.html', form=form)


# TODO: Create the dashboard page that will display the user's fitness goals, progress, and other relevant information.
# TODO: Within the dashboard, allow users to update their fitness goals and create an assessment. This will use the BS modal popup.
@main.route('/dashboard', methods=['GET', 'POST'])
# Ensures that the user is logged in before accessing the dashboard.
# @login_required
def dashboard():
    # Ensure that the user is logged in before accessing the dashboard.
    # if not current_user.is_authenticated:
    #     flash('Please log in to access the dashboard.', 'warning')
    #     return redirect(url_for('main.login'))

    # Define the labels for the current Status
    goal_labels = {'weight_loss': 'Weight Loss',
                   'muscle_gain': 'Muscle Gain',
                   'endurance': 'Endurance',
                   'general_wellness': 'General Wellness'}

    fitness_level_labels = {'beginner': 'Beginner',
                            'intermediate': 'Intermediate',
                            'advanced': 'Advanced'}

    exercise_availability_labels = {
        '1': '1 day',
        '2': '2 days',
        '3': '3 days',
        '4': '4 days',
        '5+': '5+ days'
    }

    return render_template('dashboard.html',
                           user=current_user,
                           fitness_level_labels=fitness_level_labels,
                           exercise_availability_labels=exercise_availability_labels)


@main.route('/logout')
@login_required
def logout():
    # Log the user out
    logout_user()
    return redirect(url_for('main.index'))  # Redirect to the index page
