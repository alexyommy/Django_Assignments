from django.db import models
import re
from datetime import datetime

from django.db.models.fields import DateField
# Create your models here.
class UserManager(models.Manager):
    def validator(self, post_data):
        errors = {}

        ALPHA_REGEX = re.compile(r'^[a-zA-Z]+$')
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if not ALPHA_REGEX.match(post_data['first_name']):
            errors['first_name'] = "First name must only include alphabetical letters."
        elif len(post_data['first_name']) < 2:
            errors['name'] = 'First name is too short.'
        if not ALPHA_REGEX.match(post_data['last_name']):
            errors['last_name'] = "Last name must only include alphabetical letters."
        elif len(post_data['last_name']) < 2:
            errors['name'] = 'Last name is too short.'
        if post_data['birthday'] == "":
            errors['birthday'] = "Birthday must be populated"
        elif post_data['birthday'] > datetime.now().strftime("%Y-%m-%d"):
            errors['birthday'] = "Invalid Birthday, Must be in the past"
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = 'Email address provided is invalid'
        if len(post_data['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters'
        elif post_data['confirm_password'] != post_data['password']:
            errors['confirm_password'] = 'Password provided must match.'
        try:
            user = User.objects.get(email = post_data['email'])
            errors['email_in_use'] = 'This email is already associated with an account.'
        except:
            pass
        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 245)
    last_name = models.CharField(max_length = 245)
    birthday = models.DateField()
    email = models.CharField(max_length = 350)
    password = models.CharField(max_length = 60)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()