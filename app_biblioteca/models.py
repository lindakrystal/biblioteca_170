from django.db import models
from django.core.exceptions import ValidationError
from datetime import date
import requests

# -------------------------
# Función de validación RUT chileno (con opción de validación en línea)
# -------------------------
def validar_rut_chileno(rut_completo):
    """
    Valida RUT chileno con formato '12.345.678-9' o '12345678-9'.
    Si la API de rut.chile está disponible, se valida también en línea.
    """
    rut_completo = rut_completo.replace(".", "").replace("-", "")
    if len(rut_completo) < 2:
        raise ValidationError("RUT demasiado corto")

    rut = rut_completo[:-1]
    dv = rut_completo[-1].upper()

    # Calcular dígito verificador
    factor = 2
    total = 0
    for digit in reversed(rut):
        total += int(digit) * factor
        factor += 1
        if factor > 7:
            factor = 2
    dv_calculado = 11 - (total % 11)
    if dv_calculado == 11:
        dv_calculado = "0"
    elif dv_calculado == 10:
        dv_calculado = "K"
    else:
        dv_calculado = str(dv_calculado)

    if dv != dv_calculado:
        raise ValidationError(f"RUT inválido: {rut}-{dv}")

    # Validación adicional (opcional) con la API pública de RUT Chile
    try:
        response = requests.get(f"https://api.libreapi.cl/rut/validate?rut={rut}-{dv}")
        if response.status_code == 200:
            data = response.json()
            if not data.get("valid"):
                raise ValidationError("El RUT no es válido según rut.chile")
    except Exception:
        # Si la API falla, continúa con la validación local
        pass


# -------------------------
# Modelos básicos
# -------------------------
class Nacionalidad(models.Model):
    pais = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nacionalidad} ({self.pais})"


class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Comuna(models.Model):
    codigo = models.CharField(max_length=5)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Direccion(models.Model):
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    calle = models.CharField(max_length=150)
    numero = models.CharField(max_length=10)
    departamento = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.calle} {self.numero}, {self.comuna}"


class Biblioteca(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    paginas = models.IntegerField()
    copias = models.IntegerField()
    biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE)
    habilitado = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo


# -------------------------
# Modelo Lector con validaciones
# -------------------------
class Lector(models.Model):
    rut = models.CharField(max_length=12, unique=True, help_text="Formato: 12.345.678-9")
    nombre = models.CharField(max_length=200)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField()
    habilitado = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} ({self.rut})"

    def clean(self):
        # Validar formato y existencia del RUT
        validar_rut_chileno(self.rut)

        # Validar edad mínima (5 años)
        hoy = date.today()
        edad = hoy.year - self.fecha_nacimiento.year - (
            (hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)
        )
        if edad < 5:
            raise ValidationError("El lector debe tener al menos 5 años de edad.")


class Prestamo(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    fecha_prestamo = models.DateTimeField()
    plazo_devolucion = models.DateTimeField()
    fecha_entrega = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Préstamo: {self.libro.titulo} a {self.lector.nombre}"
