from rest_framework import permissions


class IsAdminOrPost(permissions.BasePermission):
    def has_permission(self, request, view):
        if (
            request.method == "GET"
            and request.user.is_authenticated
            and request.user.is_superuser
        ):
            return True
        elif request.method == "POST":
            return True
        return False


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and request.user.is_superuser:
            return True
        if request.user == obj:
            return True
        return False


class IsUserAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
