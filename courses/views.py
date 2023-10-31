from .models import *
from .serializers import *
from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response



def courses(request):
    return render(request, "course.html")

class CoursesDataAPIView(APIView):

    def get(self, request):
        course_details = Courses.objects.all()
        course_details_serializer = CoursesSerializer(
                course_details, many=True)
        return Response(
                {"message": "success", 
                 "course_details": course_details_serializer.data,                   },
                status=status.HTTP_200_OK,
            )