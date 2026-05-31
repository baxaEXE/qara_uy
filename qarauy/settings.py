"""
Django settings for qarauy project.
"""

import os
from pathlib import Path

from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-+*+b1_c8doenqpz%lmoc+fm+y*1=!q^-a3k5#m08(3*n2@&$7d",
)

# PythonAnywhere: USER env var = username (e.g. developer123123)
PA_DOMAIN = os.environ.get("PYTHONANYWHERE_DOMAIN")
PA_USERNAME = os.environ.get("USER", "")
if not PA_DOMAIN and PA_USERNAME:
    PA_DOMAIN = f"{PA_USERNAME}.pythonanywhere.com"

ON_PYTHONANYWHERE = PA_DOMAIN is not None and PA_DOMAIN.endswith(".pythonanywhere.com")

DEBUG = not ON_PYTHONANYWHERE

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
if PA_DOMAIN:
    ALLOWED_HOSTS.append(PA_DOMAIN)

CSRF_TRUSTED_ORIGINS = []
if PA_DOMAIN:
    CSRF_TRUSTED_ORIGINS.append(f"https://{PA_DOMAIN}")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "catalogue",
    "pages",
    "qarauy.apps.QarauyConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "qarauy.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "qarauy.context_processors.site",
                "qarauy.context_processors.language_bar",
            ],
        },
    },
]

WSGI_APPLICATION = "qarauy.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en"
TIME_ZONE = "Asia/Tashkent"
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ("en", _("English")),
    ("ru", _("Russian")),
    ("uz", _("Uzbek")),
    ("kaa", _("Karakalpak")),
]

LOCALE_PATHS = [BASE_DIR / "locale"]

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
