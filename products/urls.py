from django.urls import path
from .views import ProductListCreateView, ProductRetrieveUpdateDestroyView, ProductStatsView


urlpatterns = [
    path('products/',
        ProductListCreateView.as_view(),
        name='products'),

    path('products/<int:pk>/',
        ProductRetrieveUpdateDestroyView.as_view(),
        name='product-detail-view'),

    path('products/stats/',
        ProductStatsView.as_view(),
        name='movie-stats-view'),

]