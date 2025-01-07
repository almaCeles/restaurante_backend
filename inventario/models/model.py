from django.db import models

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField()
    platillos = models.ManyToManyField('menu.Platillo', related_name='ingredientes')

    def __str__(self):
        return self.nombre
