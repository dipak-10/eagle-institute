from .models import *
from .serializers import *
from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

def institute(request):
    return render(request, "institute.html")

class InstituteDataAPIView(APIView):

    def get(self, request):
        institute_details = Institute.objects.all()
        institute_details_serializer = InstituteSerializer(
                institute_details, many=True)
        return Response(
                {"message": "success", 
                 "institute_details": institute_details_serializer.data,                   },
                status=status.HTTP_200_OK,
            )  


