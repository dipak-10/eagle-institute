from .models import *
from .serializers import *
from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response




class GetFooterdataAPIView(APIView):

    def get(self, request):
        footer_contact_details = FooterContactDetails.objects.all().order_by('-id').first()
        social_links_data = SocialMediaLinks.objects.all().order_by('-id').first()
        contact_details_serializer = FooterContactDetailsSerializer(footer_contact_details)
        social_links_serializer = SocialMediaLinksSerializer(social_links_data)
        return Response(
                {"message": "success", 
                 "footer_contact_details": contact_details_serializer.data,
                 'social_links_data' : social_links_serializer.data
                   },
                status=status.HTTP_200_OK,
            )  