from rest_framework import serializers
from .models import GeoLocation

class GeoLocationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=32)
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    accuracy = serializers.FloatField()
    address = serializers.CharField(max_length=120)
    status = serializers.IntegerField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return GeoLocation.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.username = validated_data.get('username', instance.username)
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get('longitude', instance.longitude)
        instance.accuracy = validated_data.get('accuracy', instance.accuracy)
        instance.address = validated_data.get('address', instance.address, default='')
        instance.status = validated_data.get('status', instance.status, default='')
        instance.save()
        return instance