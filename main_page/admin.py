from django.contrib import admin
from .models import *

class BlogModelAdmin(admin.ModelAdmin):
    list_display = ("id",'blog_image', 'blog_title', 'blog_description')

class OurVisionModelAdmin(admin.ModelAdmin):
    list_display = ("id",'vision_label', 'vision_description_line_1', 'vision_description_line_2')

class ReviewsModelAdmin(admin.ModelAdmin):
    list_display = ("id",'customer_name', 'customer_review')

class BannerImagesModelAdmin(admin.ModelAdmin):
    list_display = ("id",'banner_images')

admin.site.register(OurVision,OurVisionModelAdmin)
admin.site.register(Reviews, ReviewsModelAdmin)
admin.site.register(Blog,BlogModelAdmin)
admin.site.register(BannerImages,BannerImagesModelAdmin)


admin.site.site_header = "Eagle Institute"
admin.site.site_title  =  "Eagle Institute"
admin.site.index_title  =  "Admin"