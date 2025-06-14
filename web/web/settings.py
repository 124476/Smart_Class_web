import os
from pathlib import Path

from dotenv import load_dotenv

from django.utils.translation import gettext_lazy as _

load_dotenv()


def load_bool(name, default):
    env_value = os.getenv(name, default=str(default)).lower()
    return env_value in ("true", "yes", "1", "y", "t", "on")


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", default="no_key")

DEBUG = load_bool("DJANGO_DEBUG", True)

ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", default="*").split(",")


INSTALLED_APPS = [
    "unfold",
    "unfold.contrib.filters",
    "unfold.contrib.forms",
    "unfold.contrib.inlines",
    "unfold.contrib.import_export",
    "unfold.contrib.guardian",
    "unfold.contrib.simple_history",

    "apps.api.apps.ApiConfig",
    "apps.news.apps.NewsConfig",
    "apps.about.apps.AboutConfig",
    "apps.users.apps.UsersConfig",
    "apps.stats.apps.StatsConfig",
    "apps.foods.apps.FoodsConfig",
    "apps.objects.apps.ObjectsConfig",
    "apps.classes.apps.ClassesConfig",
    "apps.problems.apps.ProblemsConfig",
    "apps.homepage.apps.HomepageConfig",

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "active_link",
    "sorl.thumbnail",
    "allauth",
    "allauth.account",
    'widget_tweaks',
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
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "web.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "web.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation"
        ".UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation" 
        ".MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation" 
        ".CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation" 
        ".NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = "users.User"

LOGIN_URL = "/auth/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

LANGUAGE_CODE = "ru"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static_dev"]
STATIC_ROOT = "static"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

LANGUAGES = [
    ("en", _("English")),
    ("ru", _("Russian")),
]

LOCALE_PATHS = (BASE_DIR / "locale/",)

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_CHANGE_EMAIL = True

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}