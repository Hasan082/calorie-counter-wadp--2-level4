# Calorie Tracker Django Project

This is a web application built with Django for tracking daily calorie intake and managing user profiles. The project is designed for educational purposes and demonstrates user authentication, profile management, and CRUD operations for calorie entries.

## Features
- User registration and login
- Profile creation and editing (age, gender, weight, height)
- Add, view, and manage daily calorie entries
- Dashboard showing daily calorie totals and user BMR
- Secure user data (each user sees only their own data)
- Responsive UI with Bootstrap

## How It Works
- Users register and log in to access their dashboard.
- Each user has a profile storing personal data (age, weight, height, etc.).
- Users can add food items and calories consumed for each day.
- The dashboard displays the user's BMR and total calories consumed for the current day.

## Setup Instructions
1. Clone the repository:
	```bash
	git clone <repo-url>
	cd calorieTracker
	```
2. Install dependencies:
	```bash
	pip install -r requirements.txt
	```
3. Apply migrations:
	```bash
	python manage.py migrate
	```
4. Run the development server:
	```bash
	python manage.py runserver
	```
5. Access the app at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Project Structure
- `core/` — Django project settings and static files
- `calorie__counter/` — Main app with models, views, forms, templates
- `templates/` — HTML templates for pages and components
- `static/` — CSS and JS files

## Technologies Used
- Django
- SQLite (default, can be changed)
- Bootstrap 5

## Notes
- Make sure to create and update your profile after registration for accurate dashboard calculations.
- Only authenticated users can add/view calorie entries and see their dashboard.

## License
This project is for educational use and demonstration purposes.
