from django.urls import path
from .views import LendingListDetailView, LendingView, CloseLendingView, ListLendingsOfUserView, ExpiredLendingUpdateView

urlpatterns = [
    path("lending/", LendingView.as_view()),
    path("lending/<int:pk>/", LendingListDetailView.as_view()),
    path("lending/<int:pk>/user/", ListLendingsOfUserView.as_view()),
    path("lending/<int:pk>/close/", CloseLendingView.as_view()),
    path("lending/expired/", ExpiredLendingUpdateView.as_view()),
]
