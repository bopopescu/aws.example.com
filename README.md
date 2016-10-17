MOST BASIC
mkdir example.com
cd example.com
virtualenv .
source bin/activate
pip install django
pip freeze > requirements.txt
django-admin.py startproject project

SET STATIC ENVIRONMENT
cd project
mkdir static media templates
mkdir static/images static/js static/css 
mkdir templates/core mkdir templates/email-templates
cd templates/core
touch base.html footer.html footer_js.html header.html header_css.html nav.html

SET DYNAMIC SETTINGS ENVIRONMENT
mkdir project/settings
mv project/settings.py project/old_settings.py
touch project/settings/base.py project/settings/local.py project/settings/production.py

SET STANDARD APPS
python manage.py startapp core
touch core/decorators.py core/functions.py core/classes.py core/exceptions.py core/vars.py
python manage.py startapp sample_app
touch sample_app/urls.py
mkdir sample_app/templates
mkdir sample_app/templates/sample_app