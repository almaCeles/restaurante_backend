from rest_framework import generics
from ..models.model import Ingrediente
from ..serializers.ingrediente_serializer import IngredienteSerializer

class IngredienteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer

class IngredienteRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer
