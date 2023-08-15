from rest_framework import permissions

class IsDepartmentAdmin(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE':
            return request.user == obj.forecaster
        if request.method in ['POST', 'PUT', 'GET']:
            return True