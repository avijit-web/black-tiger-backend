from django.db import models
from ckeditor.fields import RichTextField



# Create your models here.
class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=20)
    website_url = models.URLField(blank=True)
    projected_monthly_budget = models.DecimalField(max_digits=10, decimal_places=2)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class ContactPageForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    


class PageMeta(models.Model):
    PAGE_CHOICES = [
        ('Home', 'Home'),
        ('About BBTAA Team', 'About BBTAA Team'),
        ('Our Services', 'Our Services'),
        ('Portfolio', 'Portfolio'),
        ('Blog', 'Blog'),
        ('Contact Us', 'Contact Us'),
    ]
    
    page_name = models.CharField(max_length=100, choices=PAGE_CHOICES, unique=True)
    meta_title = models.CharField(max_length=200)
    meta_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.page_name
    


class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio_images/')
    url = models.URLField(max_length=200, null= True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    


    

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=100)
    site_logo = models.ImageField(upload_to='site_logo/')
    fav_icon = models.ImageField()
    address = models.TextField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    whatsapp_number = models.CharField(max_length=20)
    social_media_links = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.site_name
    


class Banner(models.Model):
   
    PAGE_CHOICES = [
        ('Home', 'Home'),
        ('About BBTAA Team', 'About BBTAA Team'),
        ('Our Services', 'Our Services'),
        ('Portfolio', 'Portfolio'),
        ('Contact Us', 'Contact Us'),
    ]

    page_name = models.CharField(max_length=100, choices=PAGE_CHOICES, unique=True)
    image_alt_text = models.CharField(max_length=200, blank=True)
    banner_image_mobile = models.ImageField(upload_to='banner_images/', blank=True, null=True)
    banner_image_tablet = models.ImageField(upload_to='banner_images/', blank=True, null=True)
    banner_image_desktop = models.ImageField(upload_to='banner_images/', blank=True, null=True)
    banner_main_text_part_one = models.CharField(max_length=200, blank=True)
    banner_main_text_part_two = models.CharField(max_length=200, blank=True)
    banner_main_text_anime = models.CharField(max_length=100, blank=True)
    banner_super_text = models.CharField(max_length=200, blank=True)
    banner_sub_text = models.CharField(max_length=200, blank=True)
    button_text = models.CharField(max_length=50, blank=True)
    button_link = models.URLField(blank=True)
    video = models.FileField(upload_to='banner_videos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.page_name


class PartnerCompanyLogo(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='partner_logos/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    


class BannerVideo(models.Model):
    video = models.FileField(upload_to='banner_videos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    