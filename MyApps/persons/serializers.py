from dataclasses import field
from statistics import mode

from rest_framework import serializers
from MyApps.persons.models import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

        
class CustomerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

        
class EmployeeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
