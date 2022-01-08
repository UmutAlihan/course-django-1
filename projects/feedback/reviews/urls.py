from django.urls import path

from . import views

urlpatterns = [
    path("", views.ReviewView.as_view(), name="review"),  # as_view() is built in method, makes sure django can find get/post methods
    path("thank-you", views.ThankYouView.as_view(), name="thank-you"),
    path("reviews", views.ReviewsListView.as_view(), name="reviews-list"),
    path("reviews/<int:id>", views.SingleReviewView.as_view(), name="single-review"),
]