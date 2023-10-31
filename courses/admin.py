from django.contrib import admin
from .models import *

class CoursesModelAdmin(admin.ModelAdmin):
    list_display = ("id",'course_name', 'course_image', 'course_description_line_1', 'course_description_line_2')

admin.site.register(Courses,CoursesModelAdmin)


admin.site.site_header = "Eagle Institute"
admin.site.site_title  =  "Eagle Institute"
admin.site.index_title  =  "Admin"