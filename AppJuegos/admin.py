from django.contrib import admin
from AppJuegos.models import (
    Rol,
    RolPermission,
    Permission,
    User,
    Award,
    Game,
    Probabilidad,
    Styles,
    GameImageUpload
)

# Register your models here.

class PemissionAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
class GameImageUploadAdmin(admin.ModelAdmin):
    list_display = ('game_name', 'image_type', 'image')
    search_fields = ('game_name', 'image_type')
    list_filter = ('game_name', 'image_type')


admin.site.register(User)
admin.site.register(Rol)
admin.site.register(Permission, PemissionAdmin)
admin.site.register(RolPermission)
admin.site.register(Award)
admin.site.register(Game)
admin.site.register(Probabilidad)
admin.site.register(Styles)
admin.site.register(GameImageUpload, GameImageUploadAdmin)


