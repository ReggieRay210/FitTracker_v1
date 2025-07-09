from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, IntegerField, FloatField
from wtforms.validators import DataRequired, Email, Length, Optional, NumberRange, ValidationError, EqualTo
import re


def email_check(form, field):
    """Custom validator to check if the email is in a valid format."""
    email_regex = r'^[\w.+-]{2,}@[\w-]{2,}\.[a-z]{3,}$'
    if not re.match(email_regex, field.data):
        raise ValidationError('Invalid email format.')


def password_complexity(form, field):
    """Custom validator to check password complexity."""
    password = field.data
    if len(password) < 8:
        raise ValidationError('Password must be at least 8 characters long.')
    if password == 'password':
        raise ValidationError('Password cannot be "password".')
    if not any(char.islower() for char in password):
        raise ValidationError(
            'Password must contain at least one lowercase letter.')
    if not any(char.isupper() for char in password):
        raise ValidationError(
            'Password must contain at least one uppercase letter.')
    if not any(char.isdigit() for char in password):
        raise ValidationError('Password must contain at least one digit.')
    if not any(char in "!@#$%&()[]"for char in password):
        raise ValidationError(
            'Password must contain at least one special character (!@#$%&()[]).')


class registrationForm(FlaskForm):
    """Form for user registration."""
    name = StringField('Name', validators=[
                       DataRequired(), Length(min=2, max=80)])
    email = StringField('Email', validators=[DataRequired(), Email(),
                                             email_check])
    password = PasswordField('Password', validators=[
                             DataRequired(), password_complexity])
    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(), EqualTo('password')])

    # user fitness selection field
    goal = SelectField('Goal', choices=[
        ('weight_loss', 'Weight Loss'),
        ('muscle_gain', 'Muscle Gain'),
        ('endurance', 'Endurance'),
        ('general_wellness', 'General Wellness')],
        validators=[DataRequired()])

    fitness_level = SelectField('Fitness Level', choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced')],
        validators=[DataRequired()])

    exercise_availability = SelectField('Days per week for exercise',
                                        choices=[('1', '1 day'),
                                                 ('2', '2 days'),
                                                 ('3', '3 days'),
                                                 ('4', '4 days'),
                                                 ('5+', '5+ days')],
                                        validators=[DataRequired()])
    submit = SubmitField('Register')


class loginForm(FlaskForm):
    """Form for user login."""
    email = StringField('Email', validators=[
                        DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

    def validate_email(self, email):
        from FitTracker_app.models import User
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('Account not found. Please register.')


class assessmentForm(FlaskForm):
    """Form for user assessment."""
    weight = FloatField('Weight (lbs)', validators=[Optional(), NumberRange(min=0)])
    age = IntegerField('Age', validators=[Optional(), NumberRange(min=0)])

    push_ups = IntegerField('Push-ups (in 1 minute)', validators=[Optional(), NumberRange(min=0)])
    sit_ups = IntegerField('Sit-ups (in 1 minute)', validators=[Optional(), NumberRange(min=0)])
    squats = IntegerField('Squats (in 1 minute)', validators=[Optional(), NumberRange(min=0)])
    restingHeartRate = IntegerField('Resting Heart Rate (BPM)', validators=[Optional(), NumberRange(min=30, max=200)])
    halfMileTime = FloatField('Half-Mile Time (minutes)', validators=[Optional(), NumberRange(min=1)])

    shoulders = FloatField('Shoulders (inches)', validators=[Optional(), NumberRange(min=0)])
    chest = FloatField('Chest (inches)', validators=[Optional(), NumberRange(min=0)])
    biceps = FloatField('Biceps (inches)', validators=[Optional(), NumberRange(min=0)])
    forearms = FloatField('Forearms (inches)', validators=[Optional(), NumberRange(min=0)])
    waist = FloatField('Waist (inches)', validators=[Optional(), NumberRange(min=0)])
    hips = FloatField('Hips (inches)', validators=[Optional(), NumberRange(min=0)])
    thigh = FloatField('Thighs (inches)', validators=[Optional(), NumberRange(min=0)])
    calves = FloatField('Calves (inches)', validators=[Optional(), NumberRange(min=0)])

    submit = SubmitField('Complete Assessment')

class updateGoalForm(FlaskForm):
    """Form for updating user fitness goals and information."""
    goal = SelectField('Goal', choices=[
        ('weight_loss', 'Weight Loss'),
        ('muscle_gain', 'Muscle Gain'),
        ('endurance', 'Endurance'),
        ('general_wellness', 'General Wellness')],
        validators=[DataRequired()])

    fitness_level = SelectField('Fitness Level', choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced')],
        validators=[DataRequired()])

    exercise_availability = SelectField('Days per week for exercise',
                                        choices=[('1', '1 day'),
                                                 ('2', '2 days'),
                                                 ('3', '3 days'),
                                                 ('4', '4 days'),
                                                 ('5+', '5+ days')],
                                        validators=[DataRequired()])
    submit = SubmitField('Update Goals')


# TODO: Create assessment form to allow user to input their fitness assessment data.
