from django.db import models
from time import strftime
from datetime import datetime

# Create your models here.
class showManager(models.Manager):
    def validate(self, form):
        errors = {}

        if len(form['title']) < 2:
            errors['title'] = "Show title should be at least 2 characters"
        if len(form['network']) < 3:
            errors['network'] = "Show network should be at least 3 characters"
        if len(form['desc']) < 10:
            errors['desc'] = "Description should be at least 10 characters"
        if len(form['release_date']) == 0:
            errors['release_date'] = "Date must be entered"
        elif datetime.strptime(form['release_date'], '%Y-%m-%d') > datetime.now():
            errors['release_date'] = "Release Date should be in the past"
        return errors

class show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release_date = models.DateTimeField()
    desc = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = showManager()




