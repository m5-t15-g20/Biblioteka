from django.urls import path
from .views import *


urlpatterns = [
    path("books/", BookView.as_view()),
    path("books/<int:pk>/", BookDetailedView.as_view()),
    path("favorites/<int:pk>/", FavoriteView.as_view()),
]
