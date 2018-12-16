## User POC

Requirement `python3.6` or greater

```bash
python -m venv .venv
.venv/bin/activate
pip install -r requirements.txt
```

Change into source directory

```bash
cd src
```

Initialise and setup the db
```bash
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

Startup the application with
```bash
python app.py
```

`/register` your user and if you would like to be admin head to `/make_me_admin`

This should demonstrate the basic controls required for a simple application
