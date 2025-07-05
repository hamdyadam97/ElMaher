from .dev import *
ROOT_URLCONF = 'project.urls_admin'
ALLOWED_HOSTS = ['admin.localhost', 'localhost']
SESSION_COOKIE_DOMAIN = 'admin.localhost'
CSRF_TRUSTED_ORIGINS = ['http://admin.localhost:8001']

