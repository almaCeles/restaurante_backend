from django.db import models

class Mesa(models.Model):
    numero = models.IntegerField(unique=True)
    capacidad = models.IntegerField()

    def __str__(self):
        return f"Mesa {self.numero}"

class Pedido(models.Model):
    mesa = models.ForeignKey(Mesa, on_delete=models.SET_NULL, null=True)
    platillos = models.ManyToManyField('menu.Platillo',  related_name="platillos")
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado = models.CharField(max_length=20, choices=[('Pendiente', 'Pendiente'), ('Servido', 'Servido')])

    def calcular_total(self):
        return sum(platillo.precio for platillo in self.platillos.all())
