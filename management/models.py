from django.db import models
from django.core.exceptions import ValidationError

class Founder(models.Model):
    founder_name = models.CharField(max_length=10000)
    founder_image = models.ImageField(upload_to='static/founder_images')

    class Meta:
        verbose_name = 'Founder Detail'
    


class Branch(models.Model):
    branch_name = models.CharField(max_length=10000)
    branch_address = models.CharField(max_length=10000)
    branch_image = models.ImageField(upload_to = 'static/branch_images')
    branch_contact_number_1 = models.CharField(max_length=10000)
    branch_contact_number_2 = models.CharField(max_length=10000, blank=True, null=True)

    class Meta:
        verbose_name = 'Branch Detail'

    def __str__(self):
        return self.branch_name
    

class HodPersonModel(models.Model):
    hod_name = models.CharField(max_length=10000)
    hod_image = models.ImageField(upload_to='static/hod_images')

    class Meta:
        verbose_name = 'Hod Person'
    
    def __str__(self):
        return self.hod_name
    


class HodDetailsModel(models.Model):
    barnch_name = models.ForeignKey(Branch, on_delete=models.CASCADE)
    hod_names = models.ManyToManyField(HodPersonModel)
    class Meta:
        verbose_name = 'Hod Details'
    
    



    
    
