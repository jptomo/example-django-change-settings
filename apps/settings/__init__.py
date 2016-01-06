DEBUG = True

SECRET_KEY = 'some secret'

ROOT_URLCONF = 'apps.main'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
