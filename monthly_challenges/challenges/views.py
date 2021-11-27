from django.http import HttpResponse, HttpResponseNotFound


# Create your views here

def monthly_challenge_by_number(request, month):
    return HttpResponse(month)

def monthly_challenge(request, month):
    ## month -> is the identifier as defined in brackets from challenges/urls.py
    ## multiple <..> dynamic url parameters -> can be extracted simply by name as parameters in view function (as kywargs)
    challenge_text = None
    if month == "january":
        challenge_text = 'eat no meat for entire month'
    elif month == "february":
        challenge_text = 'walk for at least 20 mins a day'
    elif month == "march":
        challenge_text = 'march text is here'
    else:
        return HttpResponseNotFound('<h1>This month is not supported</h1>')
    return HttpResponse(challenge_text)
