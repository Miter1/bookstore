from django.db import models
from django.contrib.auth.models import User
# Create your models here.
"""
Data migration is the process of selecting, preparing, extracting,
and transforming data and permanently transferring it from one
computer storage system to another.

'python manage.py makemigrations': command to create migrations
(script to write changes to a database)
Migrations are stored in 'migrations' folder

'python manage.py migrate': command to write data to a database
by corresponding migrations.
"""
class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField(blank=True, null=True)
    biography = models.TextField(max_length=5000, blank=True)
    # CharField: field to store a text
    # max_length: maximum length of text in a field
    # TextField: field to store multiline text

    # __str__(): returns a string which represents a model
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
class Book(models.Model):
    title = models.CharField(max_length=255)
    # ForeighKey: refers to a another model
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField(blank=True, null=True)
    price = models.FloatField(default=0)
    image = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
class Letter(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    text = models.TextField(max_length=5000)
    # 'auto_now=True' sets a current date and time value to the field
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.email}'
    
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    date_time = models.DateTimeField(auto_now=True)