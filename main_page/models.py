from django.db import models
from django.utils.html import mark_safe



class OurVision(models.Model):
    vision_image = models.ImageField(upload_to='static/vision_image')
    vision_label = models.CharField(max_length=1000)
    vision_description_line_1 = models.CharField(max_length = 10000)
    vision_description_line_2 = models.CharField(max_length=10000)
    vision_description_line_3 = models.CharField(max_length = 10000, blank=True, null=True)
    vision_description_line_4 = models.CharField(max_length = 10000, blank=True, null=True)

    class Meta:
        verbose_name = 'Vision Content'

class Reviews(models.Model):
    customer_image = models.ImageField(upload_to='static/vision_image', blank=True, null = True)
    customer_name = models.CharField(max_length = 10000)
    customer_review = models.CharField(max_length = 10000)

    class Meta:
        verbose_name = 'Customer Review'

class Blog(models.Model):
    blog_image = models.ImageField(upload_to = 'static/blog_images')
    blog_title = models.CharField(max_length = 20000)
    blog_description = models.CharField(max_length = 10000)

    class Meta:
        verbose_name = 'Blog Detail'

class BannerImages(models.Model):
    banner_images = models.ImageField(upload_to = 'static/banner_images')

    class Meta:
        verbose_name = 'Banner Image'

    def image_preview(self):
        if self.banner_images:
            return f'<img src="{self.banner_images.url}" style="max-width:100px; max-height:100px;" />'
        else:
            return 'No Image'

    image_preview.short_description = 'Image Preview'
