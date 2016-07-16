
## Create project
```
django-admin startproject myapi .
```
## Configure project
All Configuration in myapi/settings.py

### Postgres setup

Add:
```
DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': 'postgres',
       'USER': 'postgres',
       'PASSWORD': 'changethis_masterpostgres_pwd',
       'HOST': 'postgres',
       'PORT': 5432,
   }

}

Run migrate command afterwards ( from commandline ).
```
## Database setup
### Migrations
For each update to `members/models.py`
```
python manage.py makemigrations members
python manage.py migrate members
```

### Querying database
Doc: https://docs.djangoproject.com/ja/1.9/topics/db/queries/

#### Create object and save it to database at the end.
```
>>> from members.models import Member
>>> Member.objects.all()
[]
>>> m = Member(first_name="Erik", last_name="Kaareng-Sunde", email="esu@enonic.com")
>>> m.save()
>>> Member.objects.get(id=1).first_name
'Erik'
>>> Member.objects.get(last_name="Kaareng-Sunde").first_name
'Erik'
>>>
```

#### Direct insertion in database
```
>>> from members.models import Member
>>> Member.objects.create(first_name="Erik", last_name="Kaareng-Sunde", email="esu@enonic.com")
```

### Create a model of an existing Database
```
 python manage.py inspectdb
```

## logging
```
import logging
LOG = logging.getLogger(__name__)
```
## Django interactive shell
```
python manage.py shell
```


## Run server in dev mode
```
python manage.py runserver 0.0.0.0:8000
```

## Tips and tricks

### Python debuger

```
pip install pudb
```


## Use modules outside of django projects
In main.pi
```
import django
import os

os.environ['DJANGO_SETTING_MODULE'] = "myapi.settings"

# Do something!

```
## Mail logging in django
https://github.com/anymail/django-anymail

In settings.py
```
# Email sending with mailgun
ANYMAIL = {
    'MAILGUN_API_KEY': '<your key here>',
    "MAILGUN_SEND_DEFAULTS": {
        "esp_extra": {"sender_domain": "<mailgun sender>"}
    },
}
EMAIL_BACKEND = "anymail.backends.mailgun.MailgunBackend"
DEFAULT_FROM_EMAIL = "django_sender@mg.enonic.com"

```

In code
```
>>> from django.core.mail import send_mail
>>> send_mail("mail from django","this is a email from django","django <django@enonic.com>",["esu@enonic.com"])
```
## uwsgi

- uwsgi and nginx: http://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html
