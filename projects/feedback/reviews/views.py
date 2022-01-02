from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ReviewForm

# Create your views here.

def review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST) # pass request to ReviewForm constructor

        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect("/thank-you")
            # results new get request from client, which calls thank_you view and returns that rendered html page
    else:
        form = ReviewForm()

    return render(request, "reviews/review.html", {
                "form": form
            })


# mostly POST requests dont return rendered html page, instead redirects to another page
def thank_you(request):
    return render(request, 'reviews/thank_you.html')
