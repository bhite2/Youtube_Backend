# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xo&s_xf(9!v1c&5mj11e(-_to-l1*=48e5&*t*4hyzw6u98)z2'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'youtube_database',
        "USER": 'root',
        "PASSWORD": '#Ma23As17',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}