from django.urls import path

from . import views

urlpatterns = [
    path("", views.ReviewView.as_view(), name="review"),  # as_view() is built in method, makes sure django can find get/post methods
    path("thank-you", views.thank_you)
]