from django.contrib import admin
from .models import User, Rol, Permission, RolPermission

# Register your models here.

class PemissionAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(User)
admin.site.register(Rol)
admin.site.register(Permission, PemissionAdmin)
admin.site.register(RolPermission)


