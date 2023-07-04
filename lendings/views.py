from .models import Lending
from .serializers import LeadingSerializer
from rest_framework.generics import ListCreateAPIView, ListAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView
from users.permissions import IsUserAdmin, IsOwnerOrAdmin
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from users.models import User
from copies.models import Copy
from rest_framework.views import Response
# import ipdb


class LendingView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserAdmin]
    lookup_field = "pk"

    queryset = Lending.objects.all()
    serializer_class = LeadingSerializer

    def perform_create(self, serializer):
        user_id = self.request.data.pop("user")
        user = get_object_or_404(User, pk=user_id)
        copy_id = self.request.data.pop("copy")
        copy = get_object_or_404(Copy, pk=copy_id)
        # ipdb.set_trace()
        serializer.save(user=user, copy=copy)


class LendingListDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrAdmin]
    lookup_field = "pk"

    queryset = Lending.objects.all()
    serializer_class = LeadingSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


# class LendingUpdateDetailView(UpdateAPIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsUserAdmin]
#     lookup_field = "pk"

#     queryset = Lending.objects.all()
#     serializer_class = LeadingSerializer
