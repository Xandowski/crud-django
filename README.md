# A crud in Django using docker

clone the repository

```
git clone https://github.com/Xandowski/crud-django.git
```
optional: create a viurtalenv

```
python3 -m venv .venv
source .venv/bin/activate
```

then generate the .env file

```
python3 contrib/env_gen.py
```

and do the migrate

```
python3 manage.py migrate
```

the folder structure should be look like this:

```
.
├── Dockerfile
├── README.md
├── contrib
│   └── env_gen.py
├── db.sqlite3
├── docker-compose.yml
├── docs
│   └── README.md
├── manage.py
├── payment
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   ├── settings.cpython-310.pyc
│   │   ├── urls.cpython-310.pyc
│   │   └── wsgi.cpython-310.pyc
│   ├── asgi.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-310.pyc
│   │   │   ├── admin.cpython-310.pyc
│   │   │   ├── apps.cpython-310.pyc
│   │   │   ├── models.cpython-310.pyc
│   │   │   ├── urls.cpython-310.pyc
│   │   │   └── views.cpython-310.pyc
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   │   ├── __init__.py
│   │   │   └── __pycache__
│   │   │       └── __init__.cpython-310.pyc
│   │   ├── models.py
│   │   ├── templates
│   │   │   └── index.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── requirements.txt
```

the run the docker command:

```
docker compose up
or
docker-compose up
```

this will bring up the django applicantion, postgres and adminer 

for more information see [docs](/docs) folder
