from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import UserSerializer
from .models import User
from .permissions import IsOwnerOrAdmin, IsAdminOrPost

from django.contrib.auth.hashers import make_password


class UserView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrPost]

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrAdmin]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_update(self, serializer):
        if "password" in self.request.data:
            password = make_password(self.request.data["password"])
            serializer.save(password=password)
        else:
            serializer.save()
