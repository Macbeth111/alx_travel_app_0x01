from rest_framework import serializers
from .models import PropertyType, Location, Property
from .models import TravelDestination


class TravelDestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelDestination
        fields = '__all__'


class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyType
        fields = ['id', 'name']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'city', 'region']


class PropertySerializer(serializers.ModelSerializer):
    property_type = PropertyTypeSerializer(read_only=True)
    location = LocationSerializer(read_only=True)

    class Meta:
        model = Property
        fields = ['id', 'title', 'description', 'price',
                  'property_type', 'location', 'created_at']
