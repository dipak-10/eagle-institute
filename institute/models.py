from django.db import models

# Create your models here.

class Institute(models.Model):
    label = models.CharField(max_length=1000)
    description_line_1 = models.CharField(max_length=10000)
    description_line_2 = models.CharField(max_length=10000)
    description_line_3 = models.CharField(max_length=10000, blank=True, null=True)
    description_line_4 = models.CharField(max_length=10000, blank=True, null=True)
    institute_image = models.ImageField(upload_to='static/institute_images')

    class Meta:
        verbose_name = 'Institute Facilities'
