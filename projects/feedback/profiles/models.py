from django.db import models

# Create your models here.

class UserProfile(models.Model):
    # it only stores the path to the file in the database
    image = models.FileField(upload_to="images")
