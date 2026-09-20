from django.urls import path
from . import ProductListCreateView, ProductRetrieveUpdateDestroyView


urlpatterns = [
    path('products/',
        ProductListCreateView.as_view(),
        name='products'),

    path('products/<int:pk>/',
        ProductRetrieveUpdateDestroyView.as_view(),
        name='product-detail-view'),

]