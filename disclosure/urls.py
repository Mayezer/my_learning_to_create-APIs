from django.urls import path
from .views import DisclosureListCreateView, DisclosureRetrieveUpdateDestroyView


urlpatterns = [
    path('disclosure/',
        DisclosureListCreateView.as_view(),
        name='disclosure'),

    path('disclosure/<int:pk>/',
        DisclosureRetrieveUpdateDestroyView.as_view(),
        name='disclosure-detail-view'),

]