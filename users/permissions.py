from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

class AdminOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == 0


class IsNotAuthenticated(BasePermission):
    def has_permission(self, request, view):
        valide = request.user.is_authenticated
        return(not valide)


class OwnerOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        valide = request.user.is_authenticated
        if valide:
            return(obj == request.user)
        return False


        