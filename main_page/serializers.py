from rest_framework import serializers
from .models import *

class OurVisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurVision
        fields = "__all__"



class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"

class BannerImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerImages
        fields = "__all__"