from django.contrib import admin

from .models import Post, Author, Tag


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date",) # have to be exactly same field names as in models.py
    list_display = ("title", "author", "date",)
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
