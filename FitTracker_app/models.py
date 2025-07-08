from flask_login import UserMixin
from FitTracker_app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    # user's fitness data
    goal = db.Column(db.String(50))
    fitness_level = db.Column(db.String(50))
    exercise_availability = db.Column(db.String(50))

    # User progression tracking
    weight = db.Column(db.Float, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    push_ups = db.Column(db.Integer, nullable=True)
    sit_ups = db.Column(db.Integer, nullable=True)
    squats = db.Column(db.Integer, nullable=True)
    resting_heart_rate = db.Column(db.Integer, nullable=True)
    half_mile_time = db.Column(db.Float, nullable=True)

    # body measurements
    shoulders = db.Column(db.Float, nullable=True)
    chest = db.Column(db.Float, nullable=True)
    biceps = db.Column(db.Float, nullable=True)
    forearms = db.Column(db.Float, nullable=True)
    waist = db.Column(db.Float, nullable=True)
    hips = db.Column(db.Float, nullable=True)
    thighs = db.Column(db.Float, nullable=True)
    calves = db.Column(db.Float, nullable=True)

    def set_password(self, password):
        """Set the user's password."""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Check the user's password."""
        return check_password_hash(self.password, password)

    def completed_assessment(self):
        """Check if the user has completed the assessment."""
        return all([
            self.weight is not None,
            self.age is not None,
            self.push_ups is not None,
            self.sit_ups is not None,
            self.squats is not None,
            self.resting_heart_rate is not None,
            self.half_mile_time is not None,
            self.shoulders is not None,
            self.chest is not None,
            self.biceps is not None,
            self.forearms is not None,
            self.waist is not None,
            self.hips is not None,
            self.thighs is not None,
            self.calves is not None,
        ])

    def __repr__(self):
        return f'<User {self.name}>'
