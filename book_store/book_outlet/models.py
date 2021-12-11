from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

# models: data entities: blueprint for the database objects

class Book(models.Model):
    title = models.CharField(max_length=255) # field type
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    #created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.rating}"