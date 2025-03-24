<h3>library_Management_System</h3><br><h5>Project Description</h5><br>This is a Library Management System built using Django and Django REST Framework (DRF).It provides RESTful API endpoints for managing books and user authentication.<br><h5>Setup instructions</h5><br>
1.	Clone the Repository
•	git clone https://github.com/username/library_Management_System.git
2.	Create virtual environment and activate it.
•	python -m venv myenv
•	venv\Scripts\activate
3.	Installed Required dependencies
•	Django (4.2.16)
•	Djangorestframework (3.15.2)
•	djangorestframework_simplejwt (5.5.0)
•	dotenv
•	PyMySQL
•	MySQL Workbench (8.0 CE)
•	postman
4.	Setup Environment Variables
•	Create an .env file in the project root and add following variables.
•	SECRET_KEY = ”Your-secret-key”
•	DATABASE_NAME =  “library_db”
•	DATABASE_USER = “root”
•	DATABASE_PASSWORD = ”Your_password”
•	Ensure load the dotenv file in settings.py
5.	Apply Migrations
•	python manage.py makemigrations
•	python manage.py migrate
6.	Run the server
•	python manage.py runserver
7.	Test API Endpoints
•	http://127.0.0.1:8000/api/admin/signup/<br><h5>Project Structure Explanation</h5><br>
o	Library_Management_System/     # Root Project Directory
•	books/                     	   # Main Django App
•	migrations/                    # Database migration files
•	__init__.py                    # Marks as a Python package
•	admin.py                       # Django Admin configurations
•	apps.py                        # App configuration
•	models.py                      # Database Models (Book, User)
•	serializers.py                 # DRF Serializers for API
•	urls.py                        # URL routing for the app
•	views.py                       # API Views (CRUD operations)
o	Library/                       # Django Project Directory
•	init__.py                      # Marks as a Python package
•	settings.py                    # Project settings (Database, Installed apps)
•	urls.py                        # Main project URL configurations
•	wsgi.py                        # WSGI entry point for deployment
•	asgi.py                        # ASGI entry point for async handling
•	.env                           # Environment variables (SECRET_KEY, DB credentials)
•	manage.py                      # Django management script (migrations, runserver, etc.)
o	venv/                          # Virtual Environment (dependencies isolated)


