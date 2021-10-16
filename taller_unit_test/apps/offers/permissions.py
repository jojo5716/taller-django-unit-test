from rest_framework import permissions

class UpdateOfferPermission(permissions.BasePermission):
    """ Allow update offers """

    def has_object_permission(self, request, view, obj):
        """ If offer is expired we can't update it """
        is_request_save_method = request.method in permissions.SAFE_METHODS
        
        return is_request_save_method and not obj.is_expired