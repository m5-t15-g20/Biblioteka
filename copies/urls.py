from django.urls import path
from .views import *


urlpatterns = [
    path("copies/", CopyView.as_view()),
    path("copies/<int:pk>/", CopyDetailViews.as_view()),
]
