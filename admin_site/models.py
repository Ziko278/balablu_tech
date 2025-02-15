from django.db import models
from admin_site.model_info import *


class SiteInfoModel(models.Model):
    name = models.CharField(max_length=150)
    short_name = models.CharField(max_length=50)
    mobile_1 = models.CharField(max_length=20)
    mobile_2 = models.CharField(max_length=20, null=True, blank=True)
    emergency_contact = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=255, null=True, blank=True)

    logo = models.FileField(upload_to='images/setting/logo')
    favicon = models.FileField(upload_to='images/setting/logo', null=True, blank=True)
    preloader = models.FileField(upload_to='images/setting/logo', null=True, blank=True)

    # social media handles
    whatsapp_number = models.CharField(max_length=100, null=True, blank=True)
    facebook_handle = models.CharField(max_length=100, null=True, blank=True)
    twitter_handle = models.CharField(max_length=100, null=True, blank=True)
    linkedin_handle = models.CharField(max_length=100, null=True, blank=True)
    youtube_handle = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.short_name.upper()


class GeneralSettingModel(models.Model):
    site_in_maintenance = models.BooleanField(default=False)
    auto_user_account = models.BooleanField(default=False)
    patient_registration_without_payment = models.BooleanField(default=False)
    allow_user_login = models.BooleanField(default=False)
    auto_generate_staff_id = models.BooleanField(default=True)
    auto_generate_card_number = models.BooleanField(default=True)


class DaysModel(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name.upper()

