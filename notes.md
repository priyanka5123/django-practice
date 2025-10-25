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
After creating view, urls.py , modify urls.py again run server. Then output is Helloworld at http://127.0.0.1:8000/members/
Create a templates folder inside the members folder, and create a HTML file named myfirst.html.
python manage.py migrate
python manage.py runserver
check at http://127.0.0.1:8000/members/
