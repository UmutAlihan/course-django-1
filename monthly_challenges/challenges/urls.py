from django.urls import path

# Create your views here.
#from monthly_challenges.challenges import views
from . import views

urlpatterns = [
    path('january', views.january),
    path('february', views.february),
]