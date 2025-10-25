first create a folder and navigate to it and then create vitual env 
python -m venv menv
menv\Scripts\activate
python -m pip install Django
create first project
django-admin startproject my_tennis_club
Run the server
python manage.py runserver
create the app
python manage.py startapp members
