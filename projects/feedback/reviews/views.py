from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

from .forms import ReviewForm
from .models import Review

# Create your views here.

class ReviewView(FormView):
    # lets django know which form class should be used for rendering on this view and validating input data
    form_class = ReviewForm
    template_name = "reviews/review.html"
    # redirects to this url after form submission
    success_url = "/thank-you"

    def form_valid(self, form):
        # this method is called when the form is valid
        # we can do anything here, like saving the form data to a database
        # or sending it to a third party service
        # for example, we could send it to a custom API
        form.save()
        return super().form_valid(form)

    """def get(self, request):
        form = ReviewForm()

        return render(request, "reviews/review.html", {
            "form": form
        })

    def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")

        return render(request, "reviews/review.html", {
            "form": form
        })"""


"""def review(request):
    if request.method == "POST":
        #existing_data = Review.objects.get(pk=1) # for updating use this and set "instance=existing_data" keyw arg above
        form = ReviewForm(request.POST) #, instance=existing_data) # pass request to ReviewForm constructor

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
            # results new get request from client, which calls thank_you view and returns that rendered html page
    else:
        form = ReviewForm()

    return render(request, "reviews/review.html", {
                "form": form
            })"""

class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        ### this returns the context data as dictionary same as render() method
        ### you can additionally pass context data to the template
        context = super().get_context_data(**kwargs)
        context["message"] = "Thank you for your review!"
        return context


"""# mostly POST requests dont return rendered html page, instead redirects to another page
def thank_you(request):
    return render(request, 'reviews/thank_you.html')
"""


class ReviewsListView(ListView):
    template_name = "reviews/reviews_list.html"
    # django will fetch data for us from Review model
    # dont instantiate just point to the model class
    model = Review
    # use can use this to override the default value of "object_list" on template
    context_object_name = "reviews"

"""    def get_queryset(self):
        # returns all reviews
        base_query = super().get_queryset()
        # filter by rating before sending query to db
        data = base_query.filter(rating__gte=4)
        return data"""

class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review
    # you can use your model name instead of "object" on template
