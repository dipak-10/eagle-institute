from django.db import models

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


