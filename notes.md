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

