from .prod import *

ROOT_URLCONF = 'project.urls_frontend'
ALLOWED_HOSTS = ['awael-sa.com', 'www.awael-sa.com',  'https://awael-sa.com',
    'https://www.awael-sa.com',]
SESSION_COOKIE_DOMAIN = '.awael-sa.com'
# CSRF_TRUSTED_ORIGINS = ['https://www.awael-sa.com']


CSRF_TRUSTED_ORIGINS = [
    'https://awael-sa.com',
    'https://www.awael-sa.com',
]

