from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from app_biblioteca.views import inicio

# -------------------------------
# Importaciones para Swagger
# -------------------------------
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# -------------------------------
# Configuración del esquema DRF
# -------------------------------
schema_view = get_schema_view(
    openapi.Info(
        title="app_biblioteca API",
        default_version='v1',
        description="Documentación de la API de mi proyecto",
        contact=openapi.Contact(email="kfincheira@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

# -------------------------------
# URLs del proyecto
# -------------------------------
urlpatterns = [
    path('', lambda request: redirect('login/'), name='root'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),

    path('inicio/', inicio, name='inicio'),  # página principal protegida

    path('admin/', admin.site.urls),
    path('app_biblioteca/', include('app_biblioteca.urls')),

    # Documentación de la API
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
