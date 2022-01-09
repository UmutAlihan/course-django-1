from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

# Create your views here.


def store_file(file):



class CreateProfileView(View):
    def get(self, request):
        return render(request, "profiles/create_profile.html")

    def post(self, request):
        # request.FILES -> gives access to uploaded files
        # this comes from template form name="image"
        # multiple assigned names can retrieve multiple files
        print(request.FILES["image"])
        return HttpResponseRedirect("/profiles")

