from __future__ import unicode_literals

from django.db import models

# Create your models here.

# http://stackoverflow.com/questions/1512059/django-get-an-object-form-the-db-or-none-if-nothing-matches 
class GetOrNoneManager(models.Manager):
    #Adds get_or_none method to objects
    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            return None