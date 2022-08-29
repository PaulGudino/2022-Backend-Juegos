from django.contrib import admin
from .models import User, Rol, Section, Permission, RolPermission, UserRol

# Register your models here.

admin.site.register(User)
admin.site.register(Rol)
admin.site.register(Section)
admin.site.register(Permission)
admin.site.register(RolPermission)
admin.site.register(UserRol)


