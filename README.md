# Students-API
This is a RESTful API for managing student data that allows users to perform CRUD (Create, Read, Update, Delete) operations.

# Features
. View a list of students
. View a specific student by id
. Add a new student to the database
. Update an existing student's information
. Delete a student from the database

# Tech Stack
The following technologies were used to create this API:

. Flask (Python web framework)
. Flask-RESTful (RESTful API extension for Flask)
. SQLAlchemy (database toolkit for Python)

# Installation
. Clone this repository.
. Navigate to the project directory in your terminal.
. Create a virtual environment and activate it. (Optional)
. Install dependencies: pip install -r requirements.txt
. Rename the .env.example file to .env, and set the database URI.
. Create database tables: python manage.py create_db
. Run the application: python manage.py runserver`

# API Endpoints
Endpoint	HTTP Method	CRUD Method	Result
/students	GET	READ	Get all students
/students/<id>	GET	READ	Get a single student by ID
/students	POST	CREATE	Add a new student
/students/<id>	PUT	UPDATE	Update information for a student
/students/<id>	DELETE	DELETE	Delete a student

# Handling Errors
The API returns JSON error responses if something goes wrong. The following HTTP status codes are used:

. 400 - Bad Request
. 404 - Not Found
. 500 - Internal Server Error

# Authors
Alexander Chulu
chulualexandar@gmail.com
-- Initial work

# License
This project is licensed under the MIT License - see the LICENSE.md file for details.
