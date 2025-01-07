from rest_framework import serializers
from menu.models import Platillo
from inventario.models.model import Ingrediente
from ..models import Mesa, Pedido
from menu.serializers.menu_serializer import PlatilloSerializer

class PedidoSerializer(serializers.ModelSerializer):
    platillos = PlatilloSerializer(many=True)
    mesa = serializers.PrimaryKeyRelatedField(queryset=Mesa.objects.all())

    class Meta:
        model = Pedido
        fields = '__all__'

    def create(self, validated_data):
        platillos_data = validated_data.pop('platillos')
        pedido = Pedido.objects.create(**validated_data)
        for platillo_data in platillos_data:
            pedido.platillos.add(platillo_data)
        pedido.total = pedido.calcular_total()
        pedido.save()
        return pedido

class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields = '__all__'
