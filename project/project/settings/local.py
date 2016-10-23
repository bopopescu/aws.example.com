from django.conf import settings

if settings.DEBUG:
	# import os
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

	STATIC_URL = '/static/'

	MEDIA_URL = '/media/'