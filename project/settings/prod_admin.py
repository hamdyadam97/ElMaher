from .dev import *
ROOT_URLCONF = 'project.urls_admin'
ALLOWED_HOSTS = ['admin.awael-sa.com', 'www.admin.awael-sa.com',  'https://admin.awael-sa.com',
    'https://www.admin.awael-sa.com',]
SESSION_COOKIE_DOMAIN = '.awael-sa.com'
# CSRF_TRUSTED_ORIGINS = ['https://admin.awael-sa.com']


CSRF_TRUSTED_ORIGINS = [
    'https://admin.awael-sa.com',
    'https://www.admin.awael-sa.com',
]
