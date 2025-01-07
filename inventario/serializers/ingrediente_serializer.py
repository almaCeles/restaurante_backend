from rest_framework import serializers
from ..models.model import Ingrediente
from menu.models import Platillo

class IngredienteSerializer(serializers.ModelSerializer):
    platillos = serializers.PrimaryKeyRelatedField(queryset=Platillo.objects.all(), many=True)

    class Meta:
        model = Ingrediente
        fields = ['id', 'nombre', 'cantidad', 'platillos']
