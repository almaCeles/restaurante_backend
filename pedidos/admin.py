from django.contrib import admin

# Register your models here.
from .models import Mesa, Pedido

admin.site.register(Mesa)
admin.site.register(Pedido)
