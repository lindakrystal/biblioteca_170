from django.urls import path, include
from rest_framework import routers
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from .views import (
    inicio,
    registro,
    logout_view,  # 👈 tu función personalizada
    NacionalidadViewSet,
    AutorViewSet,
    ComunaViewSet,
    DireccionViewSet,
    BibliotecaViewSet,
    LibroViewSet,
    LectorViewSet,
    PrestamoViewSet,
)

# -------------------------------
# Redirigir raíz al login
# -------------------------------
def home(request):
    return redirect('login')

# -------------------------------
# Router DRF (rutas API REST)
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
# URLs principales
# -------------------------------
urlpatterns = [
    # Redirección raíz
    path('', home, name='home'),

    # Vistas HTML
    path('inicio/', inicio, name='inicio'),
    path('registro/', registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    # 👇 Aquí reemplazamos la vista por defecto por tu función personalizada
    path('logout/', logout_view, name='logout'),

    # API REST Framework
    path('', include(router.urls)),

    # Navegador DRF (opcional, útil en desarrollo)
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
