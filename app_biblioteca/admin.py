from django.contrib import admin
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

@admin.register(Lector)
class LectorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'rut', 'digito_verificador', 'biblioteca', 'habilitado')

@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('libro', 'lector', 'fecha_prestamo', 'plazo_devolucion', 'fecha_entrega')
