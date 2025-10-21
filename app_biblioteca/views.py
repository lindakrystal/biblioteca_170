from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Nacionalidad, Autor, Comuna, Direccion, Biblioteca, Libro, Lector, Prestamo
from .serializer import (
    NacionalidadSerializer,
    AutorSerializer,
    ComunaSerializer,
    DireccionSerializer,
    BibliotecaSerializer,
    LibroSerializer,
    LectorSerializer,
    PrestamoSerializer
)

# -------------------------------
# Vistas HTML
# -------------------------------
@login_required(login_url='/login/')
def inicio(request):
    """Vista principal protegida: solo usuarios logueados pueden entrar."""

    # Guardar mensaje de bienvenida en la sesión si no existe
    if 'mensaje_bienvenida' not in request.session:
        request.session['mensaje_bienvenida'] = f'¡Bienvenido {request.user.username}!'

    # Obtener mensaje desde la sesión
    mensaje_bienvenida = request.session.get('mensaje_bienvenida')

    # Eliminar mensaje para que solo se muestre una vez
    if 'mensaje_bienvenida' in request.session:
        del request.session['mensaje_bienvenida']

    return render(request, 'inicio.html', {'message': mensaje_bienvenida})


def registro(request):
    """Permite registrar nuevos usuarios."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # inicia sesión automáticamente
            messages.success(request, "Registro Exitoso. ¡Bienvenido!")
            return redirect('inicio')  # redirige al inicio
        else:
            messages.error(request, "No ha sido posible registrarlo. Revise el formulario por errores.")
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

# -------------------------------
# Configuración de autenticación DRF
# -------------------------------
auth_classes = [SessionAuthentication, BasicAuthentication]
perm_classes = [IsAuthenticated]

# -------------------------------
# ViewSets DRF (CRUD API)
# -------------------------------
class NacionalidadViewSet(viewsets.ModelViewSet):
    queryset = Nacionalidad.objects.all()
    serializer_class = NacionalidadSerializer
    authentication_classes = auth_classes
    permission_classes = perm_classes

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    authentication_classes = auth_classes
    permission_classes = perm_classes

class ComunaViewSet(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer
    authentication_classes = auth_classes
    permission_classes = perm_classes

class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer
    authentication_classes = auth_classes
    permission_classes = perm_classes

class BibliotecaViewSet(viewsets.ModelViewSet):
    queryset = Biblioteca.objects.all()
    serializer_class = BibliotecaSerializer
    authentication_classes = auth_classes
    permission_classes = perm_classes

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    authentication_classes = auth_classes
    permission_classes = perm_classes

class LectorViewSet(viewsets.ModelViewSet):
    queryset = Lector.objects.all()
    serializer_class = LectorSerializer
    authentication_classes = auth_classes
    permission_classes = perm_classes

class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
    authentication_classes = auth_classes
    permission_classes = perm_classes
