from django.urls import path
from .views import LendingListDetailView, LendingUpdateDetailView, LendingView

urlpatterns = [
    path("lending/", LendingView.as_view()),
    path("lending/<int:pk>/", LendingListDetailView.as_view()),
    path("lending/<int:pk>/", LendingUpdateDetailView.as_view()),
]
