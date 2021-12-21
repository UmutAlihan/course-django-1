from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

# models: data entities: blueprint for the database objects

class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2)


class Address(models.Model):
    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.street}, {self.postal_code}, {self.city}'

    class Meta:
        # add behaviours to models, registering special settings, which affect how the model is used
        verbose_name_plural = 'Address Entries'

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)#, related_name="author") , null=True, blank=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

# doing cross_query:
# books_by_rowling = Book.objects.filter(author__last_name__contains="wling")
# inverse relation query:
# jkr = Author.objects.get(first_name="J.K.")
# jkr.book_set.all() # class name of related model alır, lower case yapar ve "_set" ekleyerek attribute oluşturur objene
# yada related_name option kullanılabilir (book_set yerine)
# jkr.books.filter(rating__gt=2)


class Book(models.Model):
    title = models.CharField(max_length=255) # field type
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books") # NULL allows book with no authors
    # CASCADE: any deletion of the author will also delete the book
    # PROTECT: any deletion of the author will raise an error
    # SET_NULL: any deletion of the author will set the author to null
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True) # Harry Potter 1 => harry-potter-1
    ## configuring admin are from here is not recommended
    ## use these ares to configure DB-side
    #created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)
    published_countries = models.ManyToManyField(Country, related_name="books")
        # no on_delete option for manytomany field
        # holding the data in a separate table instead using inefficient list data structure
        # on delete -> django only removes connection in that mapping table
        # on add new data ->  author_x.published_countries.add(germany)

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    def save(self, *args, **kwargs): # group all positiional and keyword arguments
        self.slug = slugify(self.title)
        super().save(*args, **kwargs) # making sure save method is still getting called

    def __str__(self):
        return f"{self.title} - {self.rating}"


# Book.objects.filter(is_bestselling=True)
# filter: Book.objects.filter(is_bestselling=True, rating__gte=2)
# filter: Book.objects.filter(is_bestselling=True, rating__gte=2, title__contains="Lord")

# from django.db.models import Q
# OR: Book.objects.filter(Q(rating__lte=3) | Q(is_bestselling=True))
# AND: Book.objects.filter(Q(rating__lte=3) | Q(is_bestselling=True), Q(author="J.K. Rowling"))




# bestsellers = Book.objects.filter(is_bestselling=True)