from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView

from .forms import ReviewForm
from .models import Review

# Create your views here.

class ReviewView(View):
    def get(self, request):
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
        })


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


class ReviewsListView(TemplateView):
    template_name = "reviews/reviews_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context["reviews"] = reviews
        return context