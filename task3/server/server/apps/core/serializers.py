from rest_framework import serializers

from .models import FuelPrice, FuelType, FuelStation, AdditionalService


class FuelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelType
        fields = "__all__"


class FuelPriceSerializer(serializers.ModelSerializer):
    fuel_type = FuelTypeSerializer()

    class Meta:
        model = FuelPrice
        fields = ["price", "currency", "fuel_type"]


class AdditionalServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalService
        fields = "__all__"


class FuelStationSerializer(serializers.ModelSerializer):
    services = AdditionalServiceSerializer(many=True)
    fuels = FuelPriceSerializer(many=True, source="prices")

    class Meta:
        model = FuelStation
        fields = ["id", "coordinate_x", "coordinate_y", "address", "image_urls", "fuels", "services"]
