# from _typeshed import FileDescriptor
from django.db import models

# Create your models here.
class book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(default="N/A")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    notes = models.TextField(default="N/A")
    books = models.ManyToManyField(book, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)