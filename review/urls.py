from django.urls import path
from . import ReviewListCreateView, ReviewRetrieveUpdateDestroyView


urlpatterns = [
    path('review/',
        ReviewListCreateView.as_view(),
        name='review'),

    path('review/<int:pk>/',
        ReviewRetrieveUpdateDestroyView.as_view(),
        name='review-detail-view'),

]
