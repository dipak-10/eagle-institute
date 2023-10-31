from django.contrib import admin
from .models import *

class InstituteModelAdmin(admin.ModelAdmin):
    list_display = ("id",'label', 'description_line_1', 'description_line_2')

admin.site.register(Institute,InstituteModelAdmin)


admin.site.site_header = "Eagle Institute"
admin.site.site_title  =  "Eagle Institute"
admin.site.index_title  =  "Admin"