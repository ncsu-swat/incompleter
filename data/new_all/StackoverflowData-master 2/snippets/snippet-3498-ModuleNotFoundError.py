#Source: https://stackoverflow.com/questions/73190803/migrations-error-in-django-attributeerror-str-object-has-no-attribute-meta
from django.db import models
from django.contrib.auth.models import User

class Reader(models.Model):
    rid = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo_url = models.CharField(max_length=200, blank=True, null=True)
    bio = models.CharField(max_length=200, blank=True, null=True)
    read_books = models.ManyToManyField('book.Book', through='reads.Reads');

    class Meta:
        db_table = 'reader'
    
    def __str__(self):
        return {
            'username': self.user.username,
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
            'email': self.user.email,
            'photo_url': self.photo_url,
            'bio': self.bio,
        }