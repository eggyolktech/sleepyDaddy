# sleepyDaddy

# Creation of django project
cd C:\Users\Hin\djangodev\
myvenv\Scripts\activate
cd C:\Users\Hin\djangodev\sleepydaddy
django-admin startproject sleepydaddy

# Start of django server
python manage.py runserver 0.0.0.0:8000

# Make Migration
python manage.py makemigrations schooltrack
python manage.py check
python manage.py migrate

# Add new App
python manage.py startapp schooltrack
python manage.py makemigrations schooltrack
python manage.py check
python manage.py migrate

# Create admin user
python manage.py createsuperuser
