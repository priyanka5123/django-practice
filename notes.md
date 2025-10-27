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
create the model 
python manage.py makemigrations members
python manage.py migrate
view sql
python manage.py sqlmigrate members 0001
Add records using shell
python manage.py shell
>>> from members.models import Member
>>> Member.objects.all()
This should give you an empty QuerySet object
>>> member = Member(firstname='Emil', lastname='Refsnes')
>>> member.save()
Execute this command to see if the Member table got a member:
>>> Member.objects.all().values()
result will be shown.
Add multiple records
>>> member1 = Member(firstname='Tobias', lastname='Refsnes')
>>> member2 = Member(firstname='Linus', lastname='Refsnes')
>>> member3 = Member(firstname='Lene', lastname='Refsnes')
>>> member4 = Member(firstname='Stale', lastname='Refsnes')
>>> member5 = Member(firstname='Jane', lastname='Doe')
>>> members_list = [member1, member2, member3, member4, member5]
>>> for x in members_list:
...   x.save()

>>> Member.objects.all().values()
>>> x = Member.objects.all()[5]
update
>>> x.firstname = "Stalikken"
>>> x.save()
delete
>>> x.delete()

python manage.py createsuperuser
admin register the models
Change the string representation function, __str__() of the Member Model
Set the list_display property of the MemberAdmin class

Django’s admin styles live under
django/contrib/admin/static/admin/css/
<link rel="stylesheet" href="{% static 'admin/css/base.css' %}">
<link rel="stylesheet" href="{% static 'admin/css/responsive.css' %}">
<link rel="stylesheet" href="{% static 'admin/css/dashboard.css' %}">
If you want to apply Django’s default admin CSS to your entire app (all pages) — not just one template — you should do it in your project’s base template, which all other templates extend.
If React runs separately (like on localhost:5173 and Django runs on 127.0.0.1:8000):

Django’s admin CSS files are still available at /static/admin/css/...

You can reference them via CDN-like links to Django’s server.

In React’s public/index.html (the root HTML template):
<link rel="stylesheet" href="http://127.0.0.1:8000/static/admin/css/base.css">
<link rel="stylesheet" href="http://127.0.0.1:8000/static/admin/css/responsive.css">
<link rel="stylesheet" href="http://127.0.0.1:8000/static/admin/css/dashboard.css">
You can also import them in your root React file if you prefer code imports:

src/App.jsx:
import './App.css';

// ✅ Import Django admin CSS from your Django static server
import 'http://127.0.0.1:8000/static/admin/css/base.css';
import 'http://127.0.0.1:8000/static/admin/css/responsive.css';
import 'http://127.0.0.1:8000/static/admin/css/dashboard.css';
You can also download Django’s admin CSS once and put them inside your React src/assets/css/ folder, then import locally:

import './assets/css/base.css';
Parentheses are not allowed in if statements in Django, so when you combine and and or operators, it is important to know that parentheses are added for and but not for or.
The empty keyword can also be used if the object does not exist.
The include tag allows you to include a template inside the current template.
To add custom styles
1. STATIC_ROOT = BASE_DIR / 'productionfiles'

STATIC_URL = 'static/'

#Add this in your settings.py file:
STATICFILES_DIRS = [
    BASE_DIR / 'mystaticfiles'
]
Add this to settings.py
2.python manage.py collectstatic
3.Add mystaticfiles to your django project.

To install postgres
pip install psycopg2-binary
To serve static files
pip install whitenoise


