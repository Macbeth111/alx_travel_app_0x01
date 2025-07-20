from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TravelDestinationViewSet

router = DefaultRouter()
router.register(r'destinations', TravelDestinationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
