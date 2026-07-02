# AGENTS.md — Roof Repair (proyecto.py)

## Stack
- Django 6.0.6, Python 3.x, SQLite, Pillow 12.2.0
- Single app `leads/` (Lead model, LeadForm, cotizar view)
- Deployed on PythonAnywhere (`ambar.pythonanywhere.com`)

## Key commands
```bash
.\venv\Scripts\python.exe manage.py runserver
.\venv\Scripts\python.exe manage.py makemigrations
.\venv\Scripts\python.exe manage.py migrate
.\venv\Scripts\python.exe manage.py collectstatic
.\venv\Scripts\python.exe manage.py test leads
```

## Virtual env
- Venv at `venv/` — activate via `.\venv\Scripts\Activate.ps1`
- No `requirements.txt` — generate with:
  ```bash
  .\venv\Scripts\python.exe -m pip freeze > requirements.txt
  ```
- Dependencies: Django, pillow, asgiref, sqlparse, tzdata

## Project structure
- `miprimerproyecto/` — Django project config (settings, urls, wsgi, asgi)
- `leads/` — single app (models, views, forms, admin, tests, templates)
- `templates/base.html` — base template; `leads/templates/` — app templates
- `static/` — dev static files; `staticfiles/` — collectstatic output (production)
- `db.sqlite3` — SQLite database (committed)

## Configuration quirks
- `DEBUG = False` even in development
- `ALLOWED_HOSTS = ['ambar.pythonanywhere.com']` — add `localhost` or `127.0.0.1` for local dev
- SMTP configured for Gmail with hardcoded credentials in `settings.py:129-135`
- SECRET_KEY hardcoded in `settings.py:23` — not production-safe
- `cotizar.html` form is missing `enctype="multipart/form-data"` — image upload will fail
- Static files collected to `staticfiles/` (STATIC_ROOT)

## Testing
- `leads/tests.py` exists but is empty — no tests written yet
- Use `.\venv\Scripts\python.exe manage.py test leads` to run app tests

## Git
- Repo initialized in `proyecto.py/` with first commit already made
- `.gitignore` excludes: `venv/`, `__pycache__/`, `*.pyc`, `db.sqlite3`, `staticfiles/`
- Never commit `.env`, `db.sqlite3`, or `venv/` (already in `.gitignore`)
- `.gitignore` also covers `proyecto.zip` and `primera_ventana/Roof_Repair.py` if desired
