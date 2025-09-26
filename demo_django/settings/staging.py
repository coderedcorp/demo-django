from .base import *  # noqa
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [os.environ["VIRTUAL_HOST"]]

SECRET_KEY = os.environ["RANDOM_SECRET_KEY"]

# Built-in email sending service provided by CodeRed Cloud.
# Change this to a different backend or SMTP server to use your own.
EMAIL_BACKEND = "django_sendmail_backend.backends.EmailBackend"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "HOST": os.environ["DB_HOST"],
        "NAME": os.environ["DB_NAME"],
        "USER": os.environ["DB_USER"],
        "PASSWORD": os.environ["DB_PASSWORD"],
        "OPTIONS": {
            "ssl": {},
            "charset": "utf8mb4",
        },
    }
}

SHOW_BANNER = "STAGING"
