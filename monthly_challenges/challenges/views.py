from django.http import HttpResponse


# Create your views here

def january(request):
    return HttpResponse('eat no meat for entire month')

def february(request):
    return HttpResponse('walk for at least 20 mins a day')