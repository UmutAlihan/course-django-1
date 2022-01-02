from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def review(request):
    if request.method == "POST":
        entered_username = request.POST.get('username')
        # post holds a dictionary where:
            # keys are the names of the form fields
            # values are the entered values
        if entered_username == ""\
                and len(entered_username) >= 100:
            return render(request, "reviews/review.html", {
                'has_error': True
            })
        return HttpResponseRedirect("/thank-you")
        # results new get request from client, which calls thank_you view and returns that rendered html page

    return render(request, "reviews/review.html", {
                'has_error': False
            })



# mostly POST requests dont return rendered html page, instead redirects to another page
def thank_you(request):
    return render(request, 'reviews/thank_you.html')
