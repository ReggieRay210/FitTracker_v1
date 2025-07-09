from flask import render_template, redirect, url_for, flash, request
from flask import current_app as app
from flask_login import login_user, logout_user, login_required, current_user
from FitTracker_app.forms import registrationForm, loginForm, updateGoalForm, assessmentForm
from FitTracker_app.models import User
from FitTracker_app import db
# This file defines the routes for the FitTracker pages that is listed in the
# templates folder.


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = registrationForm()
    if form.validate_on_submit():
        # check if account exists
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash('Account already exists. Please Login.', 'warning')
            return redirect(url_for('login'))

        # Create a new user
        user = User()
        user.name = form.name.data
        user.email = form.email.data
        user.goal = form.goal.data
        user.fitness_level = form.fitness_level.data
        user.exercise_availability = form.exercise_availability.data
        user.set_password(form.password.data)

        # Add the user to the database
        db.session.add(user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        # Redirect to login page after registration
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        # Check if the user exists.
        user = User.query.filter_by(email=form.email.data).first()
        if not user:
            flash('Account not found. Please register.', 'danger')
            return render_template('login.html', form=form)
        
        # Check if the password is correct
        if user.check_password(form.password.data):
            # Log the user in
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password. Please try again.', 'danger')
    return render_template('login.html', form=form)


# TODO: Create the dashboard page that will display the user's fitness goals, progress, and other relevant information.
# TODO: Within the dashboard, allow users to update their fitness goals and create an assessment. This will use the BS modal popup.
@app.route('/dashboard', methods=['GET', 'POST'])
# Ensures that the user is logged in before accessing the dashboard.
@login_required
def dashboard():
    # Ensure that the user is logged in before accessing the dashboard.
    if not current_user.is_authenticated:
        flash('Please log in to access the dashboard.', 'warning')
        return redirect(url_for('login'))

    # Create the update form and pre-populate with current values
    update_form = updateGoalForm()
    if request.method == 'GET':
        update_form.goal.data = current_user.goal
        update_form.fitness_level.data = current_user.fitness_level
        update_form.exercise_availability.data = current_user.exercise_availability
    
    # Handle form submission
    if update_form.validate_on_submit():
        # Update the user's information
        current_user.goal = update_form.goal.data
        current_user.fitness_level = update_form.fitness_level.data
        current_user.exercise_availability = update_form.exercise_availability.data
        
        # Save changes to database
        db.session.commit()
        
        flash('Your fitness goals have been updated successfully!', 'success')
        return redirect(url_for('dashboard'))

    # TODO: Create a route that will display the user's assessment results.
    assessment_form = assessmentForm()
    if assessment_form.validate_on_submit():
        # Save the assessment results to the database
        current_user.weight = assessment_form.weight.data
        current_user.age = assessment_form.age.data
        current_user.push_ups = assessment_form.push_ups.data
        current_user.sit_ups = assessment_form.sit_ups.data
        current_user.squats = assessment_form.squats.data
        current_user.restingHeartRate = assessment_form.restingHeartRate.data
        current_user.halfMileTime = assessment_form.halfMileTime.data
        current_user.shoulders = assessment_form.shoulders.data
        current_user.chest = assessment_form.chest.data
        current_user.biceps = assessment_form.biceps.data
        current_user.forearms = assessment_form.forearms.data
        current_user.waist = assessment_form.waist.data
        current_user.hips = assessment_form.hips.data
        current_user.thigh = assessment_form.thigh.data
        current_user.calves = assessment_form.calves.data
        db.session.commit()
        flash('Your assessment has been saved successfully!', 'success')
        return redirect(url_for('dashboard'))
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
                           update_form=update_form,
                           goal_labels=goal_labels,
                           fitness_level_labels=fitness_level_labels,
                           exercise_availability_labels=exercise_availability_labels)


@app.route('/logout')
@login_required
def logout():
    # Log the user out
    logout_user()
    return redirect(url_for('index'))  # Redirect to the index page
