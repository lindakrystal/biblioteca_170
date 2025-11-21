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

# -------------------------------------
# VISTAS HTML
# -------------------------------------
@login_required(login_url='/login/')
def inicio(request):
    """Vista principal protegida."""
    if 'mensaje_bienvenida' not in request.session:
        request.session['mensaje_bienvenida'] = f'¡Bienvenido {request.user.username}!'
    mensaje_bienvenida = request.session.get('mensaje_bienvenida')
    if 'mensaje_bienvenida' in request.session:
        del request.session['mensaje_bienvenida']
    return render(request, 'inicio.html', {'message': mensaje_bienvenida})


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro exitoso. ¡Bienvenido!")
            return redirect('inicio')
        else:
            messages.error(request, "Error en el formulario.")
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})


def logout_view(request):
    """Cierra sesión con mensaje."""
    logout(request)
    messages.info(request, "Has cerrado sesión exitosamente.")
    return redirect('login')


# -------------------------------------
# CONFIGURACIÓN DRF
# -------------------------------------
auth_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
perm_classes = [IsAuthenticated]


# -------------------------------------
# VIEWSETS con FILTERS
# -------------------------------------
class NacionalidadViewSet(viewsets.ModelViewSet):
    queryset = Nacionalidad.objects.all()
    serializer_class = NacionalidadSerializer
    authentication_classes = auth_classes
    permission_classes = perm_classes

    # filtros
    filterset_fields = ['pais', 'nacionalidad']
    search_fields = ['pais', 'nacionalidad']
    ordering_fields = ['pais', 'nacionalidad']


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    authentication_classes = auth_classes
    permission_classes = perm_classes

    filterset_fields = ['nacionalidad']
    search_fields = ['nombre']
    ordering_fields = ['nombre']


class ComunaViewSet(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer
    authentication_classes = auth_classes
    permission_classes = perm_classes

    filterset_fields = ['codigo', 'nombre']
    search_fields = ['nombre']
    ordering_fields = ['nombre']


class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer
    authentication_classes = auth_classes
    permission_classes = perm_classes

    filterset_fields = ['comuna']
    search_fields = ['calle']
    ordering_fields = ['calle', 'numero']


class BibliotecaViewSet(viewsets.ModelViewSet):
    queryset = Biblioteca.objects.all()
    serializer_class = BibliotecaSerializer
    authentication_classes = auth_classes
    permission_classes = perm_classes

    filterset_fields = ['direccion__comuna']
    search_fields = ['nombre']
    ordering_fields = ['nombre']


class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    authentication_classes = auth_classes
    permission_classes = perm_classes

    filterset_fields = ['autor', 'biblioteca', 'habilitado']
    search_fields = ['titulo']
    ordering_fields = ['titulo', 'paginas', 'copias']


# -------------------------------------
# LECTOR CON VALIDACIONES ESPECIALES
# -------------------------------------
class LectorViewSet(viewsets.ModelViewSet):
    queryset = Lector.objects.all()
    serializer_class = LectorSerializer
    authentication_classes = auth_classes
    permission_classes = perm_classes

    filterset_fields = ['biblioteca', 'habilitado']
    search_fields = ['nombre', 'rut']
    ordering_fields = ['nombre', 'rut']

    def create(self, request, *args, **kwargs):
        """Sobrescribe POST para validar edad + rut correctamente."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            lector = Lector(**serializer.validated_data)
            lector.clean()  # 🟢 valida RUT + edad
            lector.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"error": e.messages}, status=status.HTTP_400_BAD_REQUEST)


class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
    authentication_classes = auth_classes
    permission_classes = perm_classes

    filterset_fields = ['libro', 'lector']
    search_fields = ['libro__titulo', 'lector__nombre']
    ordering_fields = ['fecha_prestamo', 'plazo_devolucion']
