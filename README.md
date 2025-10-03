<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/python-3.12+-blue">
  <img alt="Django" src="https://img.shields.io/badge/Django-5.x-green">
  <img alt="DRF" src="https://img.shields.io/badge/DRF-3.x-red">
</p>

# Storefront

## Descripton

A fully-functional learning project built with **Django** and **Django REST Framework** — from models and auth to APIs, admin, tests, and deployment.

**Status:** Learning / non-commercial. Built as part of a course.

## Tech Stack

- **Backend**: Python, Django (5.x), Django REST Framework (3.x)
- **DB**: PostgreSQL (recommended), SQLite for quick start
- **Auth**: Session/Token/JWT
- **Ops**: pip + venv (personal choice for this particular project, otherwise feel free to use any other like Poetry, uv, Pipenv, etc.)
- **Version Control**: Git and GitHub

## Features

- Django models with a relational DB (PostgreSQL)
- Django Admin customization for quick data management
- Complete DRF API: serialization, validation, auth, filtering, pagination

## Dependencies (requirements.txt)

```env
asgiref==3.9.2
Django==5.2.6
django-debug-toolbar==6.0.0
djangorestframework==3.16.1
psycopg2==2.9.10
python-decouple==3.8
sqlparse==0.5.3
```

## Quickstart (on Ubuntu)

### 1) Prerequisites
- Python 3.12+ (Ubuntu comes with Python)
- PostgreSQL 14+ (or skip and use SQLite for quick start)

### 2) Update the system
Make sure the system is up to date and upgrade all packages
```bash
sudo apt update && sudo apt upgrade -y
```
Confirm Python version
```bash
python3 --version
```

### 3) Clone and Environment
Clone the repository to your preferred local workspace
```bash
git clone git@github.com:Galchov/storefront.git
```
Create virtual environment (optionally named venv)
```bash
python3 -m venv venv
```
Make sure you activate it before installing any dependencies / packages
```bash
source venv/bin/activate
```
Install the packages from requirements.txt file
```bash
pip install -r requirements.txt
```
Confirm all packages are installed
```bash
pip list
```

### 3) Configure the Database

In the terminal run
```bash
sudo -i -u postgres
```
Once in the local postgres, go to the console/shell by running
```bash
psql
```
Create a new database
```SQL
CREATE DATABASE database_name;
```

### 4) Local settings and environment variables (Secret Key, Database credentials, DEBUG, etc.)
Inside the project on base directory level, create `.env` file where the private variables will be stored
```bash
touch .env
```
Store the variables that MUST NOT to be published
```Python
SECRET_KEY = 'your project secret key'
DEBUG = True or False
DB_ENGINE = 'database engine'
DB_NAME = 'database name'
DB_USER = 'database username'
DB_PASSWORD = 'user password'
DB_HOST = 'host name'
DB_PORT = 'port number'
```
Then in `settings.py` implement the following settings
```Python
from decouple import config

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG')

DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE'),
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}
```

### 5) Migrate, Admin, Run
**Once the settings above are properly configured let's go to building mode**

Migrate the current migrations to the new database
```bash
python manage.py migrate
```
Create the superuser to manage the admin panel
```bash
python manage.py createsuperuser
```
Start the server and have fun
```bash
python manage.py runserver
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

