from django.shortcuts import render
from datetime import date


posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpeg",
        "author": "John Doe",
        "date": date(2021, 7, 21),
        "title": "Hike in the mountains",
        "exerpt": """aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse""",
        "content": """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et 
                    dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut 
                    cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa 
                    qui officia deserunt mollit anim id est laborum."""
    }
]

# Create your views here.

def starting_page(request):
    return render(request, 'blog/index.html') # this path is template for app

def posts(request):
    return render(request, 'blog/all-posts.html')

def post_detail(request, slug):
    return render(request, 'blog/post-detail.html')