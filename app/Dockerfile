FROM python:3.4-onbuild

EXPOSE 8000 8001
#CMD ["python", "./manage.py", "runserver", "0.0.0.0:8000"]
#CMD ["uwsgi", "--http", ":8000", "--module", "myapi.wsgi"]
CMD ["uwsgi", "--ini", "uwsgi.ini"]
