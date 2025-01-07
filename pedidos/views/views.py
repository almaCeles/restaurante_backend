from rest_framework import generics
from ..models import Mesa, Pedido
from ..serializers.platillo_serializer import MesaSerializer, PedidoSerializer

class MesaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer

class MesaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer

class PedidoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class PedidoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
