from django.conf import settings

if not settings.DEBUG:
	import os
	print "--------"
	print "ON PRODUCTION"

	ALLOWED_HOSTS = ["*"] # A wildcard allows all hosts but it is not secure, change it to a domain name, IP address

	# Database
	# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
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

	STATIC_ROOT = os.path.join(settings.BASE_DIR, 'static')
	STATIC_URL = 'https://%s/static/' % settings.AWS_S3_DOMAIN

	MEDIA_ROOT = os.path.join(settings.BASE_DIR, 'media')
	MEDIA_URL = 'https://%s/media/' % settings.AWS_S3_DOMAIN

	# info for the additional security settings below can be found on the bottom lines of the file
	# additional security settings
	# 
	# SECURE_HSTS_SECONDS = 3600
	# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
	# SESSION_COOKIE_SECURE = True
	# CSRF_COOKIE_SECURE = True
	SECURE_CONTENT_TYPE_NOSNIFF = True
	SECURE_BROWSER_XSS_FILTER = True 
	CSRF_COOKIE_HTTPONLY = True
	X_FRAME_OPTIONS = "DENY"


# SECURE_CONTENT_TYPE_NOSNIFF = True
	# serves your pages with an "x-content-type-options: nosniff" header
	# prevents "mime" based attacks, meaning it instructs the browser not to override the response content-type
	

# SECURE_HSTS_SECONDS = 3600
	# # Sets "HTTP Strict-Transport-Security" header which instructs modern browsers to refuse to connect to your domain name via an insecure connection (non-SSL or regular HTTP connections which encrypts ypur webpage)
	# # Is a must when you're app is an e-commerce
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True 
	# will include the subdomains

# SECURE_BROWSER_XSS_FILTER = True 
	# prevents XSS attacks

# SESSION_COOKIE_SECURE = True
	# Should only be used when HTTPS is enabled
	# Using a secure-only session cooke makes it more difficult for network traffic sniffers to hijack user sessions

# CSRF_COOKIE_SECURE = True
	# Should only be used when HTTPS is enabled
	# Using a secure-only CSRF cooke makes it more difficult for network traffic sniffers to hijack user sessions

# CSRF_COOKIE_HTTPONLY = True
	# prevents JS on by-passing CSRF protection
	# if you are sending form request via AJAX request, your request will need to pull a value from a hidden CSRF token form instead of using a cookie

# X_FRAME_OPTIONS = "DENY" 
	# Determine whether or not if your site is allowed to be viewed on an iframe