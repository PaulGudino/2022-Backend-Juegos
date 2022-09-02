from django.contrib import admin
from .models import User, Rol, Permission, RolPermission

# Register your models here.

admin.site.register(User)
admin.site.register(Rol)
admin.site.register(Permission)
admin.site.register(RolPermission)


