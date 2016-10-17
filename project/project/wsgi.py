"""
WSGI config for project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

VENV_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

activate_env=os.path.expanduser(os.path.join(VENV_DIR, 'bin/activate_this.py'))
execfile(activate_env, dict(__file__=activate_env))

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
os.environ["DJANGO_SETTINGS_MODULE"] = "project.settings"



application = get_wsgi_application()
