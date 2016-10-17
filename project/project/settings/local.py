from django.conf import settings

if settings.DEBUG:
	import os
	print "--------"
	print "ON LOCAL"
	ALLOWED_HOSTS = []

	# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
	STATIC_PATH = os.path.join(settings.BASE_DIR, 'static')
	STATIC_URL = '/static/'
	STATICFILES_DIRS = (STATIC_PATH, )

	MEDIA_ROOT = os.path.join(settings.BASE_DIR, 'media')