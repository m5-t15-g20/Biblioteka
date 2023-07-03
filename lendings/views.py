from .models import Lending
from .serializers import LeadingSerializer
from rest_framework.generics import ListCreateAPIView, ListAPIView, UpdateAPIView
from users.permissions import IsUserAdmin, IsOwnerOrAdmin
from rest_framework_simplejwt.authentication import JWTAuthentication


class LendingView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserAdmin]
    lookup_field = "pk"

    queryset = Lending.objects.all()
    serializer_class = LeadingSerializer


class LendingListDetailView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrAdmin]
    lookup_field = "pk"

    queryset = Lending.objects.all()
    serializer_class = LeadingSerializer


class LendingUpdateDetailView(UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserAdmin]
    lookup_field = "pk"

    queryset = Lending.objects.all()
    serializer_class = LeadingSerializer
