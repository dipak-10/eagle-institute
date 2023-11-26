from .models import *
from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError


class FounderModelAdmin(admin.ModelAdmin):
    list_display = ("id",'founder_name', 'founder_image')

admin.site.register(Founder,FounderModelAdmin)

class BranchModelAdmin(admin.ModelAdmin):
    list_display = ("id",'branch_name', 'branch_address', 'branch_contact_number_1', 'branch_contact_number_2')

admin.site.register(Branch,BranchModelAdmin)


class HodModelAdmin(admin.ModelAdmin):
    list_display = ('id','hod_name', 'hod_image')

admin.site.register(HodPersonModel,HodModelAdmin)

class HodAdminForm(forms.ModelForm):
    class Meta:
        model = HodDetailsModel
        fields = '__all__'

    def clean(self):
        super().clean()
        try:
            if self.cleaned_data['hod_names']:
                if self.cleaned_data['hod_names'].count() < 2:
                    raise  ValidationError("Exactly 2 hod names are required.")
        except:
            raise  ValidationError("hod names are required.")
# class HodDetailsModelAdmin(admin.ModelAdmin):
#     list_display = ('id','barnch_name', 'hod_names')

#     def hod_names(self, obj):
#         return ", ".join([hod.hod_name for hod in obj.hod_names.all()])

#     hod_names.short_description = 'Hod Names'

class HodDetailsModelAdmin(admin.ModelAdmin):
    form = HodAdminForm

    def save_model(self, request, obj, form, change):
        try:
            obj.full_clean()
        except ValidationError as e:
            form._update_errors(e)

        super().save_model(request, obj, form, change)
admin.site.register(HodDetailsModel,HodDetailsModelAdmin)

admin.site.site_header = "Eagle Institute"
admin.site.site_title  =  "Eagle Institute"
admin.site.index_title  =  "Admin"