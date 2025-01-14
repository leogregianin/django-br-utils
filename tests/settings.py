DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = [
    'br_utils',
    'tests'
]

SECRET_KEY = 'spam-spam-spam-spam'

SILENCED_SYSTEM_CHECKS = ('1_7.W001', 'models.W042')