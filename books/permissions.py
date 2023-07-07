from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        elif (
            request.method == "POST"
            and request.user.is_authenticated
            and request.user.is_superuser
        ):
            return True
        elif (
            request.method == "PATCH"
            and request.user.is_authenticated
            and request.user.is_superuser
        ):
            return True
        elif (
            request.method == "DELETE"
            and request.user.is_authenticated
            and request.user.is_superuser
        ):
            return True
        return False


class IsUserAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
