__author__ = 'Ikechukwu'

from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of objects to view, edit and delete them.
    """

    def has_object_permission(self, request, view, obj):
        """
        All permissions are allowed to only Authenticated object owners.
        :param request:
        :param view:
        :param obj:
        :return:
        """
        return obj.owner == request.user
