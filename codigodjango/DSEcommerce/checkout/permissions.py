from rest_framework.permissions import BasePermission

class PermisosCheckout(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'POST':
            
            return True  
        
       
        if request.user.is_authenticated and request.user.username == obj.usuario.usuario.username:
            return True