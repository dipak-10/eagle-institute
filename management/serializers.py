from rest_framework import serializers
from .models import *


class FounderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Founder
        fields = "__all__"

class BranchDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"