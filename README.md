# assignment1-django-models-serratozkoparan
assignment1-django-models-serratozkoparan created by GitHub Classroom

Username = admin
Password = 1dragos1

to create the project and the app:
$django-admin startproject Assignment
$django-admin startapp StarWars

to create the admin:
$python manage.py createsuperuser

trying to run it before git:
$python manage.py migrate
$python manage.py runserver

sometimes I got 'That port is already in use' error when I run the server.
To kill all the processes associated with port 8000:
sudo lsof -t -i tcp:8000 | xargs kill -9

git commands:
$git add .
$git status
$git commit -m 'some message'
$git push

