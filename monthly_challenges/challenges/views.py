from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


monthly_challenges = {
    "january": 'eat no meat for entire month',
    "february": 'walk for at least 20 mins a day',
    "march": 'march text is here',
    "april": 'april challenge',
    "may": 'may challenge',
    "june": 'june challenge',
    "july": 'july challenge',
    "august": 'august challenge',
    "september": 'september challenge',
    "october": 'october challenge is here',
    "november": 'november challenge',
    "december": 'december challenge'
}

# Create your views here

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse('month-challenge', args=[month])
        list_items += f"<li><a href='{month_path}'>{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('<h1>This month is not supported</h1>')

    redirect_month = months[month - 1]
    redirect_path = reverse('monthly-challenge', args=[redirect_month])
    #builds a path: /challenge/january (january comes from args)
    # bu sayede urls.py içerisinde değiştirirsen buraya kendiliğinden yansıtılır
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    ## month -> is the identifier as defined in brackets from challenges/urls.py
    ## multiple <..> dynamic url parameters -> can be extracted simply by name as parameters in view function (as kywargs)
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html")
        ## template not found error verirse -> settings.py içerisinde template_dirs değişkeni eklenir
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound('<h1>This month is not supported</h1>')
