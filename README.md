# Sample docker django project with postgres and adminer

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

define the postgres variables on .env file.:

```
DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=postgres
```
**obs:** if you are going to use other values, you need to change on docker-compose file:

```
services:
  db:
    image: postgres
    restart: always
    container_name: postgres
    environment:
      - POSTGRES_NAME=postgres
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
```


the folder structure should be look like this:

```
.
├── Dockerfile
├── README.md
├── contrib
│   └── env_gen.py
├── docker-compose.yml
├── docs
│   └── README.md
├── manage.py
├── app
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
