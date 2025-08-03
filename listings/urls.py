from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    ListingViewSet, BookingViewSet,
    PropertyTypeViewSet, LocationViewSet, PropertyViewSet,
    TravelDestinationListView
)

# One single router with ALL your viewsets
router = DefaultRouter()
router.register(r'listings', ListingViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'property-types', PropertyTypeViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'properties', PropertyViewSet)

# Single urlpatterns list
urlpatterns = [
    path('', include(router.urls)),  # No 'api/' prefix here
    path('destinations/', TravelDestinationListView.as_view(),
         name='destination-list'),
]
