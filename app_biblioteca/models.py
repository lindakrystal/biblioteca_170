from django.db import models

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


class Lector(models.Model):
    rut = models.IntegerField()
    digito_verificador = models.CharField(max_length=1)
    nombre = models.CharField(max_length=200)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE)
    habilitado = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} ({self.rut}-{self.digito_verificador})"


class Prestamo(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    fecha_prestamo = models.DateTimeField()
    plazo_devolucion = models.DateTimeField()
    fecha_entrega = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Préstamo: {self.libro.titulo} a {self.lector.nombre}"
