@echo off

cmd /k "cd /d C:\Users\Hin\djangodev\myvenv\Scripts\ & activate & cd /d C:\Users\Hin\djangodev\sleepydaddy\ & python get_school_app_status.py %* & exit /B"

