from rest_framework import serializers
from .models import TravelDestination

class TravelDestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelDestination
        fields = '__all__'
