from django.db import models
from login_app.models import User

# Create your models here.
class MessageManager(models.Manager):
    def validator(self, POST):
        errors = {}
        if len(POST['message']) < 1:
            errors['message'] = 'Message should be at least 2 characters.'
        return errors

class Wall_Message(models.Model):
    user = models.ForeignKey(User, related_name = "user_messages", on_delete = models.CASCADE)
    message = models.TextField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user_likes = models.ManyToManyField(User, related_name='liked_posts')
    objects = MessageManager()

class CommentManager(models.Manager):
    def validator(self, POST):
        errors = {}
        if len(POST['comment']) < 1:
            errors['comment'] = 'Comment should be at least 2 characters.'
        return errors

class Comment(models.Model):
    comment = models.TextField(max_length = 255)
    message = models.ForeignKey(Wall_Message, related_name="message_comments", on_delete = models.CASCADE)
    user = models.ForeignKey(User, related_name="user_comments", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CommentManager()
