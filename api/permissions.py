from rest_framework import permissions

class IsOwnerOrEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.is_authenticated and (user.role == 'owner' or user.role == 'employee'):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return obj.restaurant == request.user.restaurant
