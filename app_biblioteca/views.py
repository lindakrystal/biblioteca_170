from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core.exceptions import ValidationError

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import (
    Nacionalidad,
    Autor,
    Comuna,
    Direccion,
    Biblioteca,
    Libro,
    Lector,
    Prestamo
)
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
# VISTAS HTML
# -------------------------------
@login_required(login_url='/login/')
def inicio(request):
    """Vista principal protegida: solo usuarios logueados pueden entrar."""
    if 'mensaje_bienvenida' not in request.session:
        request.session['mensaje_bienvenida'] = f'¡Bienvenido {request.user.username}!'
    mensaje_bienvenida = request.session.get('mensaje_bienvenida')
    if 'mensaje_bienvenida' in request.session:
        del request.session['mensaje_bienvenida']
    return render(request, 'inicio.html', {'message': mensaje_bienvenida})


def registro(request):
    """Permite registrar nuevos usuarios."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro exitoso. ¡Bienvenido!")
            return redirect('inicio')
        else:
            messages.error(request, "Error al registrar el usuario. Revise los campos.")
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})


def logout_view(request):
    """Cierra la sesión del usuario y muestra mensaje."""
    logout(request)
    messages.info(request, "Has cerrado sesión exitosamente.")
    return redirect('login')


# -------------------------------
# CONFIGURACIÓN DE AUTENTICACIÓN DRF
# -------------------------------
auth_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
perm_classes = [IsAuthenticated]


# -------------------------------
# VIEWSETS DRF (CRUD API)
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


# -------------------------------
# LECTOR CON VALIDACIONES PERSONALIZADAS
# -------------------------------
class LectorViewSet(viewsets.ModelViewSet):
    queryset = Lector.objects.all()
    serializer_class = LectorSerializer
    authentication_classes = auth_classes
    permission_classes = perm_classes

    def create(self, request, *args, **kwargs):
        """Sobrescribe POST para capturar validaciones de modelo (edad, RUT)."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            lector = Lector(**serializer.validated_data)
            lector.clean()  # Ejecuta validaciones del modelo
            lector.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"error": e.messages}, status=status.HTTP_400_BAD_REQUEST)


class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
    authentication_classes = auth_classes
    permission_classes = perm_classes
