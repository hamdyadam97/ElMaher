# project/settings/dev_frontend.py

from .dev import *
ROOT_URLCONF = 'project.urls_frontend'
ALLOWED_HOSTS = ['www.localhost', 'localhost']
SESSION_COOKIE_DOMAIN = 'www.localhost'
CSRF_TRUSTED_ORIGINS = ['http://www.localhost:8000']
