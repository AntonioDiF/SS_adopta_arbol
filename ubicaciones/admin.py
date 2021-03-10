from django.contrib import admin
from .models import Ubicacion, Region

class UbicacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'region', 'coordX', 'coordY',)
    list_display_links = ('id',)
    list_filter = ('region',)
    search_fields = ('region',)
    list_per_page = 25

class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre',)
    list_display_links = ('id', 'nombre',)
    search_fields = ('nombre',)
    list_per_page = 25

admin.site.register(Region, RegionAdmin)
admin.site.register(Ubicacion, UbicacionAdmin)