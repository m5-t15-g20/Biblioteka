from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView, Request, Response, status

from .models import Book, Favorite
from .serializers import BookSerializer, FavoriteSerializer
from .permissions import IsAdminOrReadOnly

from users.models import User


class BookView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookDetailedView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class FavoriteView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, pk: int) -> Response:
        obj = get_object_or_404(Favorite, book=pk, user=request.user)
        print(obj)
        serializer = FavoriteSerializer(data=request.data)
        return serializer

    def post(self, request: Request, pk: int) -> Response:
        user_obj = get_object_or_404(User, id=request.user.id)
        book_obj = get_object_or_404(Book, id=pk)

        serializer = FavoriteSerializer(request.data, user=user_obj, book=book_obj)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
