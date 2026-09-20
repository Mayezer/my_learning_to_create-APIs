from django.contrib import admin
from django.urls import path
from products.views import ProductView, ProductDetailView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('products/',
        ProductView.as_view(),
        name='products'),

    path('products/<int:pk>/',
        ProductDetailView.as_view(),
        name='product-detail-view'),

]
