# Django Todo App

This repository contains a simple todo list application built with [Django](https://www.djangoproject.com/). It serves as a lightweight prototype showcasing Django's authentication system and basic CRUD functionality.

## Features

- User sign up, log in and log out
- Create, edit, complete and delete todo items
- Track creation and completion timestamps
- Basic HTML templates for a minimal UI

## Running locally

1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Apply migrations and start the development server:
   ```bash
   cd django_app
   python manage.py migrate
   python manage.py runserver
   ```
3. Open <http://localhost:8000> in your browser.

## Docker

A `docker-compose.yml` file is provided for convenience:
```bash
docker-compose up --build
```

## Tests

Run the Django test suite with:
```bash
python django_app/manage.py test
```

---
This project is a simple demonstration and not intended for production use.
