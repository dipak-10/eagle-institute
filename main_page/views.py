from .models import *
from .serializers import *
from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


def index(request):
    return render(request, "index.html")

def signup(request):
    return render(request, "signup.html")

def login(request):
    return render(request, "login.html")


class OurVisionDataAPIView(APIView):

    def get(self, request):
        our_vision_details = OurVision.objects.all().order_by('-id').first()
        our_vision_details_serializer = OurVisionSerializer(our_vision_details)
        return Response(
                {"message": "success", 
                 "our_vision_details": our_vision_details_serializer.data},
                status=status.HTTP_200_OK,
            )
    
class ReviewsDataAPIView(APIView):

    def get(self, request):
        customer_review_details = Reviews.objects.all()
        customer_review_details_serializer = ReviewsSerializer(
                customer_review_details, many=True)
        return Response(
                {"message": "success", 
                 "customer_review_details": customer_review_details_serializer.data},
                status=status.HTTP_200_OK,
            )
    
class BlogDataAPIView(APIView):

    def get(self, request):
        blog_details = Blog.objects.all()
        blog_details_serializer = BlogSerializer(
                blog_details, many=True)
        return Response(
                {"message": "success", 
                 "blog_details": blog_details_serializer.data},
                status=status.HTTP_200_OK,
            )
    
class BannerImagesDataAPIView(APIView):

    def get(self, request):
        banner_images = BannerImages.objects.all()
        banner_images_serializer = BannerImagesSerializer(
                banner_images, many=True)
        return Response(
                {"message": "success", 
                 "banner_images": banner_images_serializer.data},
                status=status.HTTP_200_OK,
            )
