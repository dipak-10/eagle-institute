from . import views
from .views import *
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('signup', views.signup),
    path('login', views.login),
    path("api/our-vision-details/", OurVisionDataAPIView.as_view(), name="our-vision-data"),
    path("api/review-details/", ReviewsDataAPIView.as_view(), name="review-data"),
    path("api/blog-details/", BlogDataAPIView.as_view(), name="blog-data"),
    path("api/banner-images/", BannerImagesDataAPIView.as_view(), name="blog-data"),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)