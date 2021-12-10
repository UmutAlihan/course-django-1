from django.shortcuts import render
from datetime import date


all_posts = [
    {
        "slug": "hike-in-the-mountains_1",
        "image": "mountains.jpeg",
        "author": "John Doe",
        "date": date(2021, 7, 21),
        "title": "Hike in the mountains",
        "exerpt": """aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse""",
        "content": """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et 
                    dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut 
                    cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa 
                    qui officia deserunt mollit anim id est laborum."""
    },
    {
        "slug": "hike-in-the-mountains_2",
        "image": "mountains.jpeg",
        "author": "John Doe",
        "date": date(2021, 7, 20),
        "title": "Hike in the mountains",
        "exerpt": """aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse""",
        "content": """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et 
                dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut 
                cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa 
                qui officia deserunt mollit anim id est laborum."""
    },
    {
        "slug": "hike-in-the-mountains_3",
        "image": "mountains.jpeg",
        "author": "John Doe",
        "date": date(2020, 7, 20),
        "title": "Hike in the mountains",
        "exerpt": """aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse""",
        "content": """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et 
                dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut 
                cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa 
                qui officia deserunt mollit anim id est laborum."""
    }
]

def get_date(post):
    return post["date"]

# Create your views here.

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request=request,
                  template_name='blog/index.html',
                  context={
                      "posts": latest_posts
                  })

def posts(request):
    return render(request, 'blog/all-posts.html')

def post_detail(request, slug):
    return render(request, 'blog/post-detail.html')