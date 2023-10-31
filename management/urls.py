from . import views
from .views import *
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('management', views.management),
    path("api/founder-details/", FounderDataAPIView.as_view(), name="founder-data"),
    path("api/branch-details/", BranchDataAPIView.as_view(), name="branch-data"),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)