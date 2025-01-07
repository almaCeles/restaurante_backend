from rest_framework import generics
from ..models import  Platillo
from ..serializers.menu_serializer import  PlatilloSerializer


class PlatilloListCreateAPIView(generics.ListCreateAPIView):
    queryset = Platillo.objects.all()
    serializer_class = PlatilloSerializer

class PlatilloRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Platillo.objects.all()
    serializer_class = PlatilloSerializer
