from django.urls import path
from .views import *


urlpatterns = [
    path("books/", BookView.as_view()),
    path("books/<int:pk>/", BookDetailedView.as_view()),
    path("books/follow/<int:pk>/", BookFollowUnfollow.as_view()),
]
