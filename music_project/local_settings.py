# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'music_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password',
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3ka=r4l61$y$f2y@77u#e@wndb%a4m+3s8d)g1wwgg=+^mlr&+'