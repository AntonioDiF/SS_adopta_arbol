from django.contrib import admin
from .models import Arbol, ArbolEspecie, ArbolEstado, ArbolUbicacion

class ArbolAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'altura', 'especie', 'ubicacion', 'siembra_estado', 'pagado',)
    list_display_links = ('id', 'nombre',)
    list_filter = ('pagado',)
    search_fields = ('nombre',)
    list_per_page = 25

class ArbolEstadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre',)
    list_display_links = ('id', 'nombre',)
    search_fields = ('nombre',)
    list_per_page = 25

class ArbolUbicacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'ubicacion')
    list_display_links = ('id', 'nombre',)
    search_fields = ('nombre',)
    list_per_page = 25

class ArbolEspecieAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre',)
    list_display_links = ('id', 'nombre',)
    search_fields = ('nombre',)
    list_per_page = 25

admin.site.register(Arbol, ArbolAdmin)
admin.site.register(ArbolEstado, ArbolEstadoAdmin)
admin.site.register(ArbolUbicacion, ArbolUbicacionAdmin)
admin.site.register(ArbolEspecie, ArbolEspecieAdmin)