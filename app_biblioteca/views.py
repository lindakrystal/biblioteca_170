from django.shortcuts import render
from django.contrib.auth.decorators import login_required
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
# Vista HTML principal
# -------------------------------
@login_required(login_url='/login/')
def inicio(request):
    """Vista principal protegida: solo usuarios logueados pueden entrar."""
    return render(request, 'inicio.html')

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
