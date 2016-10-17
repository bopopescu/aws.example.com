from django.conf import settings

if settings.DEBUG:
	print "--------"
	print "ON LOCAL"
	ALLOWED_HOSTS = []
