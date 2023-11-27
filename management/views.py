from .models import *
from .serializers import *
from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

def management(request):
    return render(request, "about_Manegment.html")

class FounderDataAPIView(APIView):

    def get(self, request):
        founder_details = Founder.objects.all()
        founder_details_serializer = FounderDetailsSerializer(
                founder_details, many=True)
        return Response(
                {"message": "success", 
                 "founder_details": founder_details_serializer.data},
                status=status.HTTP_200_OK,
            )
    
class BranchDataAPIView(APIView):

    def get(self, request):
        branch_details = Branch.objects.all()
        branch_details_serializer = BranchDetailsSerializer(
                branch_details, many=True)
        return Response(
                {"message": "success", 
                 "branch_details": branch_details_serializer.data},
                status=status.HTTP_200_OK,
            )

class HodDataApiView(APIView):
    def get(self, request):
        hod_details = HodDetailsModel.objects.all()
        hod_details_serializer = HodDetailsSerializer(
                hod_details, many=True)
        return Response(
                {"message": "success", 
                 "hod_details": hod_details_serializer.data},
                status=status.HTTP_200_OK,
            )