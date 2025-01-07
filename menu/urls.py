from django.urls import path
from .views.views import CategoriaListCreateAPIView, CategoriaRetrieveUpdateDestroyAPIView, PlatilloListCreateAPIView, PlatilloRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('categorias/', CategoriaListCreateAPIView.as_view(), name='categoria_list_create'),
    path('categoria/<int:pk>/', CategoriaRetrieveUpdateDestroyAPIView.as_view(), name='categoria_detail'),
    path('platillos/', PlatilloListCreateAPIView.as_view(), name='platillo_list_create'),
    path('platillo/<int:pk>/', PlatilloRetrieveUpdateDestroyAPIView.as_view(), name='platillo_detail'),
]
