from django.urls import path

# Create your views here.
#from monthly_challenges.challenges import views
from . import views

urlpatterns = [
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge),  # <value> -> any text after /challenges/... is considered by views.mont..
]