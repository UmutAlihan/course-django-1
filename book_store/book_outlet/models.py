from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

# models: data entities: blueprint for the database objects

class Book(models.Model):
    title = models.CharField(max_length=255) # field type
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    #created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.rating}"


# Book.objects.filter(is_bestselling=True)
# filter: Book.objects.filter(is_bestselling=True, rating__gte=2)
# filter: Book.objects.filter(is_bestselling=True, rating__gte=2, title__contains="Lord")
# OR: Book.objects.filter(Q(rating__lte=3) | Q(is_bestselling=True))
# AND: Book.objects.filter(Q(rating__lte=3) | Q(is_bestselling=True), Q(author="J.K. Rowling"))

# from django.db.models import Q