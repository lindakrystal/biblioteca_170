from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from app_biblioteca.views import inicio, logout_view  # 👈 importante

# Swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Token authentication (para Postman)
from rest_framework.authtoken.views import obtain_auth_token

# -------------------------------
# Configuración Swagger
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
# URLs principales del proyecto
# -------------------------------
urlpatterns = [
    # Redirige raíz al login
    path('', lambda request: redirect('login/'), name='root'),

    # Login y logout (HTML con CSRF)
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', logout_view, name='logout'),

    # Página principal protegida
    path('inicio/', inicio, name='inicio'),

    # Admin de Django
    path('admin/', admin.site.urls),

    # Rutas de la aplicación
    path('app_biblioteca/', include('app_biblioteca.urls')),

    # Swagger / Redoc
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Login DRF (para ver navegador API)
    path('api-auth/', include('rest_framework.urls')),

    # 🔑 Endpoint para obtener token de autenticación (Postman)
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
