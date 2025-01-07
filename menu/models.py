from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Platillo(models.Model):
    nombre = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    descripcion = models.TextField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
