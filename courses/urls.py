from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('course', views.courses),
    path("api/course-details/", CoursesDataAPIView.as_view(), name="course-data"),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)