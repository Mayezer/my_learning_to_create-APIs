from django.contrib import admin
from django.urls import path
from products.views import ProductListCreateView, ProductRetrieveUpdateDestroyView
from enterprise.views import EnterpriseListCreateView, EnterpriseRetrieveUpdateDestroyView
from disclosure.views import DisclosureListCreateView, DisclosureRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('products/',
        ProductListCreateView.as_view(),
        name='products'),

    path('products/<int:pk>/',
        ProductRetrieveUpdateDestroyView.as_view(),
        name='product-detail-view'),

    path('enterprise/',
        EnterpriseListCreateView.as_view(),
        name='enterprise'),

    path('enterprise/<int:pk>/',
        EnterpriseRetrieveUpdateDestroyView.as_view(),
        name='enterprise-detail-view'),

    path('disclosure/',
        DisclosureListCreateView.as_view(),
        name='disclosure'),

    path('disclosure/<int:pk>/',
        DisclosureRetrieveUpdateDestroyView.as_view(),
        name='disclosure-detail-view'),

]
