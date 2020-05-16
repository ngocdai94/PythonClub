## Initial Setup
1. Install Python
2. Install PostgreSQL
3. Install Git

--- Start Python Virtual Enviroment ---
More Detail Here: http://congerprep.blogspot.com/2019/03/django-techreview-project.html
4. Install django
5. Install psycopg2 (if running application errors)
pip install psycopg2

## Some Python Commands
1. Activate PyThon Virtual Environment: venv\scripts\activate
2. Run the server: python manage.py runserver
3. Migrate classes to Database: 
    python manage.py makemigrations
    python manage.py migrate
4. Create a superuser: python manage.py createsuperuser
5. Run a test: python manage.py test -v 2