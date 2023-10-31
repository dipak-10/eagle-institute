from django.contrib import admin
from .models import *

class FounderModelAdmin(admin.ModelAdmin):
    list_display = ("id",'founder_name', 'founder_image')

admin.site.register(Founder,FounderModelAdmin)

class BranchModelAdmin(admin.ModelAdmin):
    list_display = ("id",'branch_name', 'branch_address', 'branch_contact_number_1', 'branch_contact_number_2')

admin.site.register(Branch,BranchModelAdmin)


admin.site.site_header = "Eagle Institute"
admin.site.site_title  =  "Eagle Institute"
admin.site.index_title  =  "Admin"