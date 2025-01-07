from django.urls import path
from .views.views import IngredienteListCreateAPIView, IngredienteRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('ingredientes/', IngredienteListCreateAPIView.as_view(), name='ingrediente_list_create'),
    path('ingrediente/<int:pk>/', IngredienteRetrieveUpdateDestroyAPIView.as_view(), name='ingrediente_detail'),
]
