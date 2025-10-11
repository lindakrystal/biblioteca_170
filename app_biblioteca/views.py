from rest_framework import viewsets
from .models import Nacionalidad, Autor, Comuna, Direccion, Biblioteca, Libro, Lector, Prestamo
from .serializer import (
    NacionalidadSerializer, AutorSerializer, ComunaSerializer, DireccionSerializer,
    BibliotecaSerializer, LibroSerializer, LectorSerializer, PrestamoSerializer
)
from django.shortcuts import render
class NacionalidadViewSet(viewsets.ModelViewSet):
    queryset = Nacionalidad.objects.all()
    serializer_class = NacionalidadSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class ComunaViewSet(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer

class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer

class BibliotecaViewSet(viewsets.ModelViewSet):
    queryset = Biblioteca.objects.all()
    serializer_class = BibliotecaSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class LectorViewSet(viewsets.ModelViewSet):
    queryset = Lector.objects.all()
    serializer_class = LectorSerializer

class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

def inicio(request):
    # Puedes enviar datos al template si quieres
    contexto = {
        "mensaje": "¡Bienvenido a la Biblioteca!"
    }
    return render(request, "inicio.html", contexto)
def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, "libros.html", {"objetos": libros, "titulo": "Libros"})

def lista_lectores(request):
    lectores = Lector.objects.all()
    return render(request, "lectores.html", {"objetos": lectores, "titulo": "Lectores"})

def lista_bibliotecas(request):
    bibliotecas = Biblioteca.objects.all()
    return render(request, "bibliotecas.html", {"objetos": bibliotecas, "titulo": "Bibliotecas"})

def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, "autores.html", {"objetos": autores, "titulo": "Autores"})

def lista_nacionalidades(request):
    nacionalidades = Nacionalidad.objects.all()
    return render(request, "nacionalidades.html", {"objetos": nacionalidades, "titulo": "Nacionalidades"})

def lista_comunas(request):
    comunas = Comuna.objects.all()
    return render(request, "comunas.html", {"objetos": comunas, "titulo": "Comunas"})

def lista_direcciones(request):
    direcciones = Direccion.objects.all()
    return render(request, "direcciones.html", {"objetos": direcciones, "titulo": "Direcciones"})

def lista_prestamos(request):
    prestamos = Prestamo.objects.all()
    return render(request, "prestamos.html", {"objetos": prestamos, "titulo": "Préstamos"})

