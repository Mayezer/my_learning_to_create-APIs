from django.contrib import admin
from django.urls import path
from products.views import ProductListCreateView, ProductRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('products/',
        ProductListCreateView.as_view(),
        name='products'),

    path('products/<int:pk>/',
        ProductRetrieveUpdateDestroyView.as_view(),
        name='product-detail-view'),

]
