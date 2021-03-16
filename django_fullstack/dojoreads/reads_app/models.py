from django.db import models
from login_app.models import User

# Create your models here.
class AuthorManager(models.Manager):

    def basic_validator(self, post_data):
        errors = {}
        if len(post_data['author_name']) < 1:
            errors['author_name'] = 'Author name should be at least two characters.'
        return errors

class Author(models.Model):
    name = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = AuthorManager()

class BookManager(models.Manager):
    
    def basic_validator(self, post_data):
        errors = {}
        try:
            Book.objects.get(title = post_data['title'])
            errors['title'] = 'A book with this title already exists!'
        except:
            pass
        if len(post_data['title']) < 1:
            errors['title'] = 'Book title should be at least two characters.'
        return errors

class Book(models.Model):
    title = models.CharField(max_length = 255)
    author = models.ForeignKey(Author, related_name = "books", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = BookManager()

class ReviewManager(models.Manager):

    def basic_validator(self, post_data):
        errors = {}
        if len(post_data['review']) < 10:
            errors['review'] = 'Review should be at least ten characters long.'
        if int(post_data['rating']) < 1 or int(post_data['rating']) > 5:
            errors['rating'] = 'Review should be 1 to 5 stars.'
        return errors

class Review(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    book = models.ForeignKey(Book, related_name = "reviews", on_delete = models.CASCADE)
    user = models.ForeignKey(User, related_name = "reviews", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ReviewManager()