from django.db import models

# Create your models here.

class FooterContactDetails(models.Model):
    about_us = models.TextField(max_length=20000)
    contact_number = models.CharField(max_length = 10000)
    email_address = models.CharField(max_length = 10000)
    address = models.CharField(max_length = 10000)
    time = models.CharField(max_length = 10000)

    class Meta:
        verbose_name = 'Contact Detail'

class SocialMediaLinks(models.Model):
    facebook = models.CharField(max_length = 10000, blank=True, null=True)
    whatsapp = models.CharField(max_length = 10000, blank=True, null = True)
    twitter = models.CharField(max_length = 10000, blank=True, null = True)
    instagram = models.CharField(max_length = 10000, blank=True, null = True)
    youtube = models.CharField(max_length = 10000, blank=True, null = True)

    class Meta:
        verbose_name = 'Social Link'
     