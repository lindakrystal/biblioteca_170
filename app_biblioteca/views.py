from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
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
# ------------------------
# -------
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
@login_required(login_url='/login/')
def inicio(request):
    return render(request, 'inicio.html')

# -------------------------------
# DRF ViewSets (Class-Based Views)
# -------------------------------
class NacionalidadViewSet(viewsets.ModelViewSet):
    queryset = Nacionalidad.objects.all()
    serializer_class = NacionalidadSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]


class ComunaViewSet(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]


class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]


class BibliotecaViewSet(viewsets.ModelViewSet):
    queryset = Biblioteca.objects.all()
    serializer_class = BibliotecaSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]


class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]


class LectorViewSet(viewsets.ModelViewSet):
    queryset = Lector.objects.all()
    serializer_class = LectorSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]


class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

