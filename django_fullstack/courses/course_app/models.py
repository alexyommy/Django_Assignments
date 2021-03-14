from django.db import models
from datetime import datetime

# Create your models here.
class courseManager(models.Manager):
    def validate(self, form):
        errors = {}

        if len(form['course_name']) == 0:
            errors['course_name'] = "Course Name must be entered"
        elif len(form['course_name']) < 5:
            errors['course_name'] = "Course Name must be at least 5 characters"
        if len(form['description']) == 0:
            errors['description'] = "Description must be entered"
        elif len(form['description']) < 15:
            errors['description'] = "Description must be at least 15 characters"
        return errors

class course(models.Model):
    course_name = models.CharField(max_length=45)
    description = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = courseManager()