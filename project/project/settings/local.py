from django.conf import settings

if settings.DEBUG:
	import os
	print "--------"
	print "ON LOCAL"
	ALLOWED_HOSTS = []

	# DATABASES = {
	# 	'default': {
	# 	    'ENGINE': 'django.db.backends.sqlite3',
	# 	    'NAME': os.path.join(settings.BASE_DIR, 'db.sqlite3'),
	# 	}
	# }

	DATABASES = {
    	'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'example_com',
        'USER': 'deanarmada',
        'PASSWORD': 'd3@narmada13',
        'HOST': 'localhost', # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
        'PORT': '', 
    	}
    }

	# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
	STATIC_PATH = os.path.join(settings.BASE_DIR, 'static')
	STATIC_URL = '/static/'
	STATICFILES_DIRS = (STATIC_PATH, )

	MEDIA_ROOT = os.path.join(settings.BASE_DIR, 'media')
	MEDIA_URL = '/media/'