from django.http import JsonResponse
from rest_framework import viewsets
from .models import TravelDestination
from .serializers import TravelDestinationSerializer

def index(request):
    return JsonResponse({"message": "Welcome to the ALX Travel API!"})

class TravelDestinationViewSet(viewsets.ModelViewSet):
    queryset = TravelDestination.objects.all()
    serializer_class = TravelDestinationSerializer
