from django.db import models

class Courses(models.Model):
    course_name = models.CharField(max_length=10000)
    course_image = models.ImageField(upload_to='static/images')
    # course_description = models.TextField(max_length=10000)
    course_description_line_1 = models.CharField(max_length=10000)
    course_description_line_2 = models.CharField(max_length=10000)
    course_description_line_3 = models.CharField(max_length=10000, blank=True, null=True)
    course_description_line_4 = models.CharField(max_length=10000, blank=True, null=True)

    class Meta:
        verbose_name = 'Course Detail'
