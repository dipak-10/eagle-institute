from django.contrib import admin
from .models import *

class FooterContactDetailsModelAdmin(admin.ModelAdmin):
    list_display = ("id",'about_us', 'contact_number', 'email_address', 'address', 'time')

class SocialMediaLinksModelAdmin(admin.ModelAdmin):
    list_display = ("id",'facebook', 'whatsapp', 'twitter', 'instagram', 'youtube')

admin.site.register(FooterContactDetails,FooterContactDetailsModelAdmin)
admin.site.register(SocialMediaLinks,SocialMediaLinksModelAdmin)


admin.site.site_header = "Eagle Institute"
admin.site.site_title  =  "Eagle Institute"
admin.site.index_title  =  "Admin"