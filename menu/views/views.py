
from rest_framework import generics
from ..models import Categoria, Platillo
from ..serializers.menu_serializer import CategoriaSerializer, PlatilloSerializer

class CategoriaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class PlatilloListCreateAPIView(generics.ListCreateAPIView):
    queryset = Platillo.objects.all()
    serializer_class = PlatilloSerializer

class PlatilloRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Platillo.objects.all()
    serializer_class = PlatilloSerializer
