from rest_framework.permissions import BasePermission

class IsBuyerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.buyer == request.user or request.user.is_staff
