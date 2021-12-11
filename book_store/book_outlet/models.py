from django.db import models

# Create your models here.

# models: data entities: blueprint for the database objects

class Book(models.Model):
    title = models.CharField(max_length=255) # field type
    rating = models.IntegerField()
    #created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)