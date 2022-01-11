from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View

from .models import Post
from .forms import CommentForm

# Create your views here.

class StartingPageView(ListView):
    template_name = 'blog/index.html' # wanna be very clear about which template for which view, therefore we overwrite "template_name"
    model = Post # the model "Post" for this view
    # required for ordered item list
    ordering = ["-date"] # you can add more items in this list
    # object_list is used on template b/c of default name of generic ListView, need to overwrite as below
    context_object_name = "posts"


    # overwrite some methods to query only specific items
    def get_query_set(self):
        queryset = super().get_query_set()
        data = queryset[:3]
        return data # return modified data which you want to continue the view


""" FUNCTION BASED VIEWS are COMMENTED OUT:
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
                  })"""


class AllPostsView(ListView):
    template_name = 'blog/all-posts.html'
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"

"""def posts(request):
    all_posts = Post.objects.all()
    return render(request=request,
                  template_name='blog/all-posts.html',
                  context={
                      "all_posts": all_posts
                  })"""


class SinglePostView(View):
    # django will auto search by slug on DetailView !!!
    # auto reaise 404 error if item not found
    template_name = 'blog/post-detail.html'
    model = Post

    def get(self, request, slug): # get the slug from request
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id")
        }
        return render(request, "blog/post-detail.html", context)

    def post(self, request, slug):  #slug is part of the url we are redirecting
        comment_form = CommentForm(request.POST) # contains the submitted data
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False) # commit=False means we don't hit the database yet, only create model instance
            comment.post = post
            comment.save() # take user input, add extra data and save edited data back to the database, then redirect
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

        # if form is invalid prepare post data by fetching again
        # for given slug
        # prepare the context and render template again
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id")
        }
        render(request, "blog/post-detail.html", context)

    """ ## COMMENTED OUT BECUASE NOT USING DETAILVIEW CLASS ANYMORE
    # in order to see additional fields from Model (e.g.: Tags)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # self.object -> Post Model object, dfetched by DetailView automatically
        context['post_tags'] = self.object.tags.all()
        # need to add extra context to pass to template for CommentForm
        context['comment_form'] = CommentForm()
        return context"""

"""def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post-detail.html', {
        "post": identified_post,
        "post_tags": identified_post.tags.all()  ## this returns list of tags so that jtemplate can iterate over it
    })"""