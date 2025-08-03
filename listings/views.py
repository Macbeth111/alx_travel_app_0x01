from .serializers import ListingSerializer, BookingSerializer
from .models import Listing, Booking
from rest_framework import viewsets
from .models import PropertyType, Location, Property
from .serializers import PropertyTypeSerializer, LocationSerializer, PropertySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TravelDestination
from .serializers import TravelDestinationSerializer


class TravelDestinationListView(APIView):
    def get(self, request):
        destinations = TravelDestination.objects.all()
        serializer = TravelDestinationSerializer(destinations, many=True)
        return Response(serializer.data)


class PropertyTypeViewSet(viewsets.ModelViewSet):
    queryset = PropertyType.objects.all()
    serializer_class = PropertyTypeSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
