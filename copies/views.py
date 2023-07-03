from rest_framework.views import Response, Request
from django.shortcuts import render
from books.permissions import IsUserAdmin
from .models import Copy
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from copies.serializers import CopySerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class CopyView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = Copy.objects.all()
    serializer_class = CopySerializers
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        copies = self.get_queryset()
        serializer = self.get_serializer(copies, many=True)
        return Response(serializer.data)
    
    def get_permissions(self):
        if self.request.method == "POST":
            self.permission_classes = [IsAuthenticated, IsUserAdmin]
        return super().get_permissions()

class CopyDetailViews(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = Copy.objects.all()
    serializer_class = CopySerializers

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAuthenticated, IsUserAdmin]
        return super().get_permissions()
    
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
    
    def get_copie(self, request: Request, pk):
        copies = Copy.objects.filter(copy=pk)
        serializer = CopySerializers(copies, many=True)
        return Response(serializer.data)