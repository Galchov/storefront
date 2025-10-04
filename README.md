<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/python-3.12+-blue">
  <img alt="Django" src="https://img.shields.io/badge/Django-5.x-green">
  <img alt="DRF" src="https://img.shields.io/badge/DRF-3.x-red">
</p>

# Storefront

## Description
A fully-functional learning project built with **Django** and **Django REST Framework** — from models and auth to APIs, admin, tests, and deployment.  
**Status:** Learning / non-commercial. Built as part of a course.

## Table of Contents
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Documentation](#documentation)
- [Quickstart](#quickstart)
- [Environment Variables](#environment-variables)
- [Database Setup (PostgreSQL)](#database-setup-postgresql)
- [Run Migrations / Admin / Server](#run-migrations--admin--server)
- [Project Structure](#project-structure)
- [License](#license)

## Tech Stack
- **Backend:** Python, Django (5.x), Django REST Framework (3.x)
- **DB:** PostgreSQL (recommended) or SQLite for quick start
- **Auth:** Session / Token / JWT (documented in API docs)
- **Tooling:** `pip` + `venv` (Poetry/uv also fine)
- **Version Control:** Git + GitHub

## Features
- Relational models (PostgreSQL)
- Django Admin customization for quick data management
- DRF API with serialization, validation, auth, filtering, pagination

## Documentation
Full documentation lives in [`docs/`](docs/index.md). Start here:
- **Overview:** [`docs/01-overview.md`](docs/01-overview.md)
- **Architecture:** [`docs/02-architecture.md`](docs/02-architecture.md)
- **Domain Models (ERD):** [`docs/03-domain-models.md`](docs/03-domain-models.md)
- **API Guide:** [`docs/04-api/endpoints.md`](docs/04-api/endpoints.md)
- **Development:** [`docs/05-development.md`](docs/05-development.md)
- **Deployment:** [`docs/09-deployment.md`](docs/09-deployment.md)

> Dependencies are pinned in [`requirements.txt`](requirements.txt).

## Quickstart
### 1) Prerequisites (Ubuntu)
- Python 3.12+
- PostgreSQL 14+ (or skip for SQLite quick start)

Update packages:
```bash
sudo apt update && sudo apt upgrade -y
```
Confirm Python version:
```bash
python3 --version
```

### 2) Clone and Environment
Clone the repository to your preferred local workspace and go to the project directory. Make sure venv is activated before installing the requirements.
```bash
git clone git@github.com:Galchov/storefront.git
cd storefront
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Confirm venv is activated and the requirements are installed by running:
```bash
pip list
```

## Environment Variables
In the project's base directory create `.env` file:
```bash
touch .env
```
And store the variables like this:
```dotenv
DEBUG=True
SECRET_KEY=change-me
ALLOWED_HOSTS=127.0.0.1,localhost

DB_ENGINE=django.db.backends.postgresql
DB_NAME=yourdb
DB_USER=youruser
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
```
Then in `settings.py` implement the following:
```Python
from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', cast=bool, default=False)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='').split(',')

DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE', default='django.db.backends.sqlite3'),
        'NAME': config('DB_NAME', default='db.sqlite3'),
        'USER': config('DB_USER', default=''),
        'PASSWORD': config('DB_PASSWORD', default=''),
        'HOST': config('DB_HOST', default=''),
        'PORT': config('DB_PORT', default=''),
    }
}
```

## Database Setup (PostgreSQL)
In the terminal switch to the postgres user and open psql:
```bash
sudo -i -u postgres
psql
```
Create DB and (optionally) a role:
```SQL
CREATE DATABASE yourdb;
-- CREATE ROLE youruser WITH LOGIN PASSWORD 'yourpassword';
-- GRANT ALL PRIVILEGES ON DATABASE yourdb TO youruser;
```
`\q` to exit, `exit` to return to your shell.

## Run Migrations / Admin / Server
**Once the settings above are properly configured move to bulding mode by running:**
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Open: http://127.0.0.1:8000/

## Project Structure
```bash
storefront/
├─ apps/                     # Django apps
├─ config/                   # settings, urls, wsgi/asgi
├─ docs/                     # extended documentation
├─ manage.py
├─ requirements.txt
└─ LICENSE
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
