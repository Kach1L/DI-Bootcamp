from rest_framework import permissions

class IsAuthenticatedAndAdmin(permissions.BasePermission):

    def has_permission(self, request, view) -> bool: # checks who is the user
        if request.method in ['GET', 'POST', 'PUT', 'DELETE']:
            return request.user.is_authenticated # True - has permission
        
        # elif request.method in ['PUT', 'DELETE']:
        #     if request.user.is_authenticated: 
        #         return request.user.is_staff # True if use is administrator

    def has_object_permission(self, request, view, obj):
        if request.method in ['PUT', 'DELETE']:
            return obj.author == request.user # True if the current user is the author of the post