from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    # db_index=True is for search engine optimization set automatically in SlugFields
    content = models.TextField(validators=[MinLengthValidator(10)])
