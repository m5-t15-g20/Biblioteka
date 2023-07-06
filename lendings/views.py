from .models import Lending
from .serializers import LeadingSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from users.permissions import IsUserAdmin, IsOwnerOrAdmin
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from users.models import User
from copies.models import Copy


class LendingView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserAdmin]

    queryset = Lending.objects.all()
    serializer_class = LeadingSerializer

    def perform_create(self, serializer):
        user_id = self.request.data.pop("user")
        user = get_object_or_404(User, pk=user_id)
        copy_id = self.request.data.pop("copy")
        copy = get_object_or_404(Copy, pk=copy_id)
        serializer.save(user=user, copy=copy)


class LendingListDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserAdmin]
    lookup_field = "pk"

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [IsOwnerOrAdmin]
        return super().get_permissions()

    queryset = Lending.objects.all()
    serializer_class = LeadingSerializer
