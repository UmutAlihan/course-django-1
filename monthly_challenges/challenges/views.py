from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('<h1>This month is not supported</h1>')

    redirect_month = months[month - 1]
    return HttpResponseRedirect(f"/challenges/{redirect_month}")

def monthly_challenge(request, month):
    ## month -> is the identifier as defined in brackets from challenges/urls.py
    ## multiple <..> dynamic url parameters -> can be extracted simply by name as parameters in view function (as kywargs)
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound('<h1>This month is not supported</h1>')
