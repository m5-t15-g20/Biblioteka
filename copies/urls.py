from django.urls import path
from .views import *


urlpatterns = [
    path("copy/", CopyView.as_view()),
    path("copy/<int:pk>/", CopyDetailViews.as_view()),
]
