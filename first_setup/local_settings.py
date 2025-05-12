# local_settings.py

ALLOWED_HOSTS = [
    '127.0.0.1',
    '192.168.0.107',
    'localhost'
]

DEBUG = True  # for local development

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'meal_dbs',
        'USER': 'postgres',
        'PASSWORD': 'tiger123#',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
