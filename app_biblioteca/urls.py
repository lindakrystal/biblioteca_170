from django.urls import path
from .views import (
    lista_libros, lista_lectores, lista_bibliotecas, lista_autores,
    lista_nacionalidades, lista_comunas, lista_direcciones, lista_prestamos
)

urlpatterns = [
    path('libros/', lista_libros, name='libros'),
    path('lectores/', lista_lectores, name='lectores'),
    path('bibliotecas/', lista_bibliotecas, name='bibliotecas'),
    path('autores/', lista_autores, name='autores'),
    path('nacionalidades/', lista_nacionalidades, name='nacionalidades'),
    path('comunas/', lista_comunas, name='comunas'),
    path('direcciones/', lista_direcciones, name='direcciones'),
    path('prestamos/', lista_prestamos, name='prestamos'),
]
