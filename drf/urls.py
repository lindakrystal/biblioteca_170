from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from app_biblioteca.views import inicio

urlpatterns = [
    path('', lambda request: redirect('login/'), name='root'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),

    path('inicio/', inicio, name='inicio'),  # <--- ruta para inicio

    path('admin/', admin.site.urls),
    path('app_biblioteca/', include('app_biblioteca.urls')),
]
