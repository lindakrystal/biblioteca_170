from django.urls import path, include
from rest_framework import routers
from .views import (
    inicio,
    NacionalidadViewSet,
    AutorViewSet,
    ComunaViewSet,
    DireccionViewSet,
    BibliotecaViewSet,
    LibroViewSet,
    LectorViewSet,
    PrestamoViewSet
)
from django.shortcuts import redirect

# -------------------------------
# Redirigir raíz al login
# -------------------------------
def home(request):
    return redirect('login')

# -------------------------------
# Router DRF
# -------------------------------
router = routers.DefaultRouter()
router.register(r'nacionalidades', NacionalidadViewSet)
router.register(r'autores', AutorViewSet)
router.register(r'comunas', ComunaViewSet)
router.register(r'direcciones', DireccionViewSet)
router.register(r'bibliotecas', BibliotecaViewSet)
router.register(r'libros', LibroViewSet)
router.register(r'lectores', LectorViewSet)
router.register(r'prestamos', PrestamoViewSet)

# -------------------------------
# URLs
# -------------------------------
urlpatterns = [
    path('', home, name='home'),
    path('inicio/', inicio, name='inicio'),
    path('', include(router.urls)),
]
