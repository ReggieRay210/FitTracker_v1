from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, IntegerField, FloatField, BooleanField
from wtforms.validators import DataRequired, Email, Length, Optional, NumberRange, ValidationError, EqualTo
import re


def email_check(form, field):
    """Custom validator to check if the email is in a valid format."""
    email_regex = r'^[\w.+-]{2,}@[\w-]{2,}\.[a-z]{3,}$'
    if not re.match(email_regex, field.data):
        raise ValidationError('Invalid email format.')


def password_complexity(form, field):
    """Custom validator to check password complexity."""
    password = field.DateRangeField
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
    email = StringField('Email', validators=[DataRequired(), Email(
        check_deliverability=True), email_check])
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
                        DataRequired(), Email(check_deliverability=True)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

    def validate_email(self, email):
        from FitTracker_app.models import User
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('Account not found. Please register.')

# TODO: Create Goal update form to allow users to update their fitness goals.
# TODO: Create assessment form to allow user to input their fitness assessment data.
