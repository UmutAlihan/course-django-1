from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=100) # automatically checks and validates for mail format

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name()


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    # db_index=True is for search engine optimization set automatically in SlugFields
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    # one-to-many relation
    # SET_NULL means if author is deleted, set post's author to null
    # related_name is used to access author's posts from Post model as "author.posts"
    tags = models.ManyToManyField(Tag)
    # add many-to-many here (not Tags) which is from developers perspective


class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    text = models.TextField(max_length=200)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")


