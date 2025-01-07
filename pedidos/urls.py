from django.urls import path
from .views.views import MesaListCreateAPIView, MesaRetrieveUpdateDestroyAPIView, PedidoListCreateAPIView, PedidoRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('mesas/', MesaListCreateAPIView.as_view(), name='mesa_list_create'),
    path('mesa/<int:pk>/', MesaRetrieveUpdateDestroyAPIView.as_view(), name='mesa_detail'),
    path('pedidos/', PedidoListCreateAPIView.as_view(), name='pedido_list_create'),
    path('pedido/<int:pk>/', PedidoRetrieveUpdateDestroyAPIView.as_view(), name='pedido_detail'),
]
