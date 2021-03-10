web:python manage.py runserver
web: gunicorn django_login/apps/register/admin.wsgi --log-file -
heroku ps:scale web=1