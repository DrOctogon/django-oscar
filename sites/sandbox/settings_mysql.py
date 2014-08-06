from settings import *

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'oscar_vagrant',
        'USER': 'travis',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# workaround for the MySQL connector till Oracle support Django 1.7
# https://code.djangoproject.com/ticket/22584
TEST_CHARSET = TEST_COLLATION = False


