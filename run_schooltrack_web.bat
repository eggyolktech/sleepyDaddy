@echo off

cmd /k "cd /d C:\Users\Hin\djangodev\myvenv\Scripts\ & activate & cd /d C:\Users\Hin\djangodev\sleepydaddy\ & python manage.py runserver 0.0.0.0:8000 %*"
