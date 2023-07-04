from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from users.permissions import IsUserAdmin
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import Response


class BookView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

    def get_permissions(self):
        if self.request.method == "POST":
            self.permission_classes = [IsAuthenticated, IsUserAdmin]
        return super().get_permissions()


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
