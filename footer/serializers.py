from rest_framework import serializers
from .models import *

class FooterContactDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterContactDetails
        fields = "__all__"


class SocialMediaLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaLinks
        fields = "__all__"