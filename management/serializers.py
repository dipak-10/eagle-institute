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
    
class HodDetailsSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance) 
        representation['barnch_name'] = instance.barnch_name.branch_name
        hod_names_values = instance.hod_names.values_list('hod_name', flat=True) 
        hod_image_values = instance.hod_names.values_list('hod_image', flat=True)  # Assuming 'name' is the field you want to display
        data_dict = {
            "name":hod_names_values,
            "image":hod_image_values
        }
        representation['hod_names'] = data_dict
        return representation

    class Meta:
        model = HodDetailsModel
        fields = ['id','barnch_name','hod_names']