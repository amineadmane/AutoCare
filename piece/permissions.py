from rest_framework.permissions import (SAFE_METHODS, BasePermission,
                                        IsAuthenticated)


class AdminOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == 0


class OwnerOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        valide = request.user.is_authenticated
        if valide:
            return(obj == request.user)
        return False

class IsAuthenticatedOrReadOnly(BasePermission):
    """
    The request is authenticated, or is a read-only request.
    """

    def has_permission(self, request, view):
        if(request.method in SAFE_METHODS):
            return True
        else:
            return request.user.is_authenticated