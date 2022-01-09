from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from .forms import ProfileForm
from .models import UserProfile


# Create your views here.


def store_file(file):
    with open('temp/' + file.name, 'wb+') as destination:
        for chunk in file.chunks():  # chunks() reads file one-by-one to avoid memory issues
            destination.write(chunk)


class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"


"""class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, "profiles/create_profile.html",
                      context= {"form": form}
                      )

    def post(self, request):
        submitted_form = ProfileForm(request.POST, request.FILES)  # create profile_form to pass data and files from request

        if submitted_form.is_valid():
            # request.FILES -> gives access to uploaded files
            # this comes from template form name="image"
            # multiple assigned names can retrieve multiple files
            print(request.FILES["user_image"])
            profile = UserProfile(image=request.FILES["user_image"])
            profile.save() # it only writes path to DB and move file to specified location
            return HttpResponseRedirect("/profiles")


        return render(request, "profiles/create_profile.html",
                      context= {"form": submitted_form}
                      )
"""


class ProfileView(ListView):
    model = UserProfile
    template_name = "profiles/user_profiles.html"
    context_object_name = "profiles"
