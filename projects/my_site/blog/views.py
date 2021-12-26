from django.shortcuts import render, get_object_or_404

from .models import Post


# Create your views here.

def starting_page(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]
    # "-" is for descending order
    # django will convert command above into an entire SQL cmd so auto-optimized
    # creates one-long seq query to get all posts including pythonic syntax
        # [-3:] -> minus syntax is not supported here
    return render(request=request,
                  template_name='blog/index.html',
                  context={
                      "posts": latest_posts
                  })

def posts(request):
    all_posts = Post.objects.all()
    return render(request=request,
                  template_name='blog/all-posts.html',
                  context={
                      "all_posts": all_posts
                  })

def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post-detail.html', {
        "post": identified_post
    })