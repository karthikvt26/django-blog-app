from django.db import models

# Create your models here.

class Author(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    dob = models.DateField('date of birth')
    interests = models.TextField()

class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    visibility_level = models.CharField(max_length=20)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
