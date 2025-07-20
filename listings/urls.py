from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PropertyTypeViewSet, LocationViewSet, PropertyViewSet
from .views import TravelDestinationListView

router = DefaultRouter()
router.register(r'property-types', PropertyTypeViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'properties', PropertyViewSet)

urlpatterns = [
    path('destinations/', TravelDestinationListView.as_view(),
         name='destination-list'),
]
