from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Book

# Create your views here.

def index(request):
    try:
        books = Book.objects.all()
    except:
        raise Http404()
    return render(request, 'book_outlet/index.html',
                  context={"books": books})

def book_detail(request, id):
    #try:
    #    book = Book.objects.get(pk=id)
    #except:
    #    return Http404()
    book = get_object_or_404(Book, pk=id)
    return render(request, 'book_outlet/book_detail.html',
                  context= {
                      "title": book.title,
                      "author": book.author,
                      "rating": book.author,
                      "is_bestseller": book.is_bestselling
                  })