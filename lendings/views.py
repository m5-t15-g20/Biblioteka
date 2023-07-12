from .models import Lending
from .serializers import LeadingSerializer, LendginCreate, UserSerializerLending
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    UpdateAPIView,
    ListAPIView,
)
from users.permissions import IsUserAdmin, IsOwnerOrAdmin
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from users.models import User
from copies.models import Copy
from books.models import Book
from datetime import date, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings


class LendingView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserAdmin]

    queryset = Lending.objects.all()
    serializer_class = LendginCreate

    def perform_create(self, serializer):
        try:
            return self.initial_data["expire_date"]
        except Exception:
            today = date.today()
            delta = timedelta(days=7)
            expire_date = today + delta

            if expire_date.weekday() == 5:
                days_to_add = 7 + expire_date.weekday() + 2
                expire_date += timedelta(days=days_to_add)
            if expire_date.weekday() == 6:
                days_to_add = 7 + expire_date.weekday() + 1
                expire_date += timedelta(days=days_to_add)

        user_id = self.request.data.pop("user")
        user = get_object_or_404(User, pk=user_id)
        copy_id = self.request.data.pop("copy")
        copy = get_object_or_404(Copy, pk=copy_id)
        serializer.save(user=user, copy=copy, expire_date=expire_date)


class LendingListDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserAdmin]
    lookup_field = "pk"

    queryset = Lending.objects.all()
    serializer_class = LeadingSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [IsOwnerOrAdmin]
        return super().get_permissions()


class CloseLendingView(UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserAdmin]
    lookup_field = "pk"

    queryset = Lending.objects.all()
    serializer_class = LeadingSerializer

    def update(self, request, *args, **kwargs):
        lending_id = self.kwargs.get("pk")
        lending = get_object_or_404(Lending, pk=lending_id)
        lending.is_close = True
        lending.save()
        copy = lending.copy
        copy.is_available = True
        copy.save()
        book = get_object_or_404(Book, pk=copy.book.id)
        user = get_object_or_404(User, pk=lending.user.id)
        subject = "O livro que você estava seguindo estar disponível!"
        message = f'O livro "{book.title}" ficou disponível para empréstimo. Não perca a chance de lê-lo!'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [user.email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        return super().update(request, *args, **kwargs)


class ListLendingsOfUserView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrAdmin]
    lookup_field = "pk"
    serializer_class = LeadingSerializer

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=self.kwargs["pk"])
        self.check_object_permissions(request, user)
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        user = get_object_or_404(User, pk=self.kwargs["pk"])
        return Lending.objects.filter(user=user)


class ExpiredLendingUpdateView(APIView):
    serializer_class = UserSerializerLending

    def post(self, request):
        lendings = Lending.objects.all()
        updated_users = []

        for lending in lendings:
            print(lending.expire_date, date.today())
            if lending.expire_date <= date.today():
                user = lending.user
                user.is_authorized = False
                user.save()
                updated_users.append(user)
        updated_users_data = [
            UserSerializerLending(user).data for user in updated_users
        ]

        return Response(
            {"updated_users": updated_users_data}, status=status.HTTP_200_OK
        )
