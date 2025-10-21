from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import Nacionalidad, Autor, Comuna, Direccion, Biblioteca, Libro, Lector, Prestamo

@admin.register(Nacionalidad)
class NacionalidadAdmin(admin.ModelAdmin):
    list_display = ('pais', 'nacionalidad')

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nacionalidad')

@admin.register(Comuna)
class ComunaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')

@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    list_display = ('calle', 'numero', 'comuna')

@admin.register(Biblioteca)
class BibliotecaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion')

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'biblioteca', 'habilitado')

# -------------------------
# Admin Lector con validación RUT chileno y edad
# -------------------------
@admin.register(Lector)
class LectorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'rut', 'fecha_nacimiento', 'biblioteca', 'habilitado')

    def save_model(self, request, obj, form, change):
        obj.full_clean()  # ejecuta clean() con validaciones
        super().save_model(request, obj, form, change)

@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('libro', 'lector', 'fecha_prestamo', 'plazo_devolucion', 'fecha_entrega')
