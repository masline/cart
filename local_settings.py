DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "c1bfbf70-d40f-4483-8db1-7bdbff79ddd4a619f052-fb8a-4eb2-9481-171c98a9d577e874f596-32b8-429e-aa12-5811b04d4f86"
NEVERCACHE_KEY = "00856f2e-4695-4445-bef3-a35d22359dfde7db16d6-7c62-438b-a2bd-8b3636dcc3ee0a864e43-c672-4af5-bd86-c0c8cb29989f"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
