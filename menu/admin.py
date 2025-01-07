from django.contrib import admin

# Register your models here.
from .models import Categoria, Platillo

admin.site.register(Categoria)
admin.site.register(Platillo)
