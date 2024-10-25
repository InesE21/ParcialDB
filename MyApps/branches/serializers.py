from dataclasses import field
from statistics import mode

from rest_framework import serializers
from MyApps.branches.models import Branch

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"

        
class BranchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"