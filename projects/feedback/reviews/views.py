from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ReviewForm
from .models import Review

# Create your views here.

def review(request):
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
            })


# mostly POST requests dont return rendered html page, instead redirects to another page
def thank_you(request):
    return render(request, 'reviews/thank_you.html')
