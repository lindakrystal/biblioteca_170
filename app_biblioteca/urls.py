from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'nacionalidades', views.NacionalidadViewSet)
router.register(r'autores', views.AutorViewSet)
router.register(r'comunas', views.ComunaViewSet)
router.register(r'direcciones', views.DireccionViewSet)
router.register(r'bibliotecas', views.BibliotecaViewSet)
router.register(r'libros', views.LibroViewSet)
router.register(r'lectores', views.LectorViewSet)
router.register(r'prestamos', views.PrestamoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', include('django.contrib.auth.urls')),  # Cambia 'accounts/' por 'login/'
    path('inicio/', views.inicio, name='inicio'),  
]