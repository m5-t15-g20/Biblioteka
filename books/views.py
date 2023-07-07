from django.shortcuts import render
from .models import Book
from .serializers import FollowingSerializer
from .serializers import BookSerializer
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from users.permissions import IsUserAdmin
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import Response, status
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict


class BookView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

    def get_permissions(self):
        if self.request.method == "POST":
            self.permission_classes = [IsAuthenticated, IsUserAdmin]
        return super().get_permissions()

    def post(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BookDetailedView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "pk"

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated, IsUserAdmin]
        return super().get_permissions()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class BookFollowUnfollow(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = Book.objects.all()
    serializer_class = FollowingSerializer
    lookup_field = "pk"

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset.first())
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        lookup_value = self.kwargs.get(self.lookup_field)
        following_books = request.user.following.all()
        book_iby_id = get_object_or_404(Book, id=lookup_value)
        user_following_book = []
        for book in following_books:
            if model_to_dict(book)["id"] == lookup_value:
                user_following_book.append(model_to_dict(book))

        if len(user_following_book):
            return Response(
                "You already follow this book", status=status.HTTP_403_FORBIDDEN
            )

        else:
            request.user.following.add(book_iby_id)
            return Response("Following Book", status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        lookup_value = self.kwargs.get(self.lookup_field)
        following_books = request.user.following.all()
        book_to_unfollow = get_object_or_404(Book, id=lookup_value)

        if book_to_unfollow in following_books:
            request.user.following.remove(book_to_unfollow)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                "You are not following this book", status=status.HTTP_404_NOT_FOUND
            )
