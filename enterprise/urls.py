from django.urls import path
from . import EnterpriseListCreateView, EnterpriseRetrieveUpdateDestroyView


urlpatterns = [
    path('enterprise/',
        EnterpriseListCreateView.as_view(),
        name='enterprise'),

    path('enterprise/<int:pk>/',
        EnterpriseRetrieveUpdateDestroyView.as_view(),
        name='enterprise-detail-view'),

]