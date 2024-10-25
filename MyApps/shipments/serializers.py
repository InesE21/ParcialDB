from dataclasses import field
from statistics import mode
from rest_framework import serializers
from MyApps.shipments.models import Correspondence, Shipping, Incident

class CorrespondenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Correspondence
        fields = "__all__"

class ShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping
        fields = "__all__"

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = "__all__"