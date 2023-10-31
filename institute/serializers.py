from rest_framework import serializers
from .models import *

class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institute
        fields = "__all__"
