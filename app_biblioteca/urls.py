from django.urls import path, include
from rest_framework import routers
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from .views import (
    inicio,
    registro,
    NacionalidadViewSet,
    AutorViewSet,
    ComunaViewSet,
    DireccionViewSet,
    BibliotecaViewSet,
    LibroViewSet,
    LectorViewSet,
    PrestamoViewSet
)

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
    # Redirección raíz
    path('', home, name='home'),

    # Vistas HTML
    path('inicio/', inicio, name='inicio'),
    path('registro/', registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # API DRF
    path('api/', include(router.urls)),
]
