from django.db import models
from login_app.models import User

# Create your models here.
class BookManager(models.Manager):
    def validator(self, POST):
        errors = {}
        if len(POST['title']) < 1:
            errors['title'] = 'Title should be at least 2 characters.'
        if len(POST['desc']) < 5:
            errors['desc'] = 'Description must be at least 5 characters.'
        return errors

# Make sure class name is Singular
class Book(models.Model):
    title = models.CharField(max_length = 255)
    desc = models.TextField(max_length=255)
    creator = models.ForeignKey(User, related_name='book_creator', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    favorited_by = models.ManyToManyField(User, related_name='user_favorites')
    objects = BookManager()