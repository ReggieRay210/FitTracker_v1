
# FitTracker_v1
FitTrack is a full-stack fitness tracker web app that allows users to log daily workouts, track progress over time, and visualize activity trends. Built with Flask, SQLite, and Bootstrap, it features secure user authentication, dynamic workout logging, and interactive filtering.

🧠 Concept:
A web app where users can log daily workouts, track exercises (e.g. sets/reps, time, distance), and monitor progress over time.

💻 Stack:
 - Backend: Python (Flask) + SQLite (or PostgreSQL if you're comfortable)

 - Frontend: HTML/CSS + JavaScript + Bootstrap 5

 - Optional Extras: Chart.js for graphs, Flask-Login for auth, WTForms for forms

✅ MVP (Minimum Viable Product) Features
 1. User Registration/Login
- Email + password authentication using Flask-Login
- Workout entry information: Fitness Goal, Current Fitness Level, Days available to exercise. 
- Protected routes for logged-in users

2. Dashboard
- Snapshot of current fitness goal
- Progress Chart Summary for visualization of progress. 
- List of current workouts to complete, with associated check-boxes.
- Button for submission

3. Workout Entry Form
- Fields: date, exercise name, category (e.g. cardio, strength), duration/sets/reps, notes
- Save to database

4. Responsive Design
- Looks good on mobile and desktop using Bootstrap 5

