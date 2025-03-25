from django.db import models
from core.mixins import SeoMixin


# Create your models here.
class ContactInfo(models.Model):
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField()
    website = models.URLField()

    def __str__(self):
        return self.address
    class Meta:
        verbose_name_plural = 'Contact Info'


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image1 = models.ImageField(upload_to='images/', null=True, blank=True)
    image2 = models.ImageField(upload_to='images/', null=True, blank=True)
    image3 = models.ImageField(upload_to='images/', null=True, blank=True)
    image4 = models.ImageField(upload_to='images/', null=True, blank=True)
    def __str__(self):
        return '{}'.format(self.name)
    class Meta:
        verbose_name_plural = 'Project Info'
        ordering = ['name']

class Employee(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', null=True, blank=True)


    def __str__(self):
        return '{}'.format(self.name)
    class Meta:
        verbose_name_plural = 'Employee'


class HomePage(SeoMixin):
    first_section_title = models.CharField(max_length=200)
    first_section_description = models.TextField()
    services_section_title = models.CharField(max_length=200,null=True,blank=True)
    services_section_description = models.TextField(null=True,blank=True)
    team_section_title = models.CharField(max_length=200,null=True,blank=True)
    team_section_description = models.TextField(null=True,blank=True)
    projects_section_title = models.CharField(max_length=200,null=True,blank=True)
    projects_section_description = models.TextField(null=True,blank=True)

    def __str__(self):
        return 'Home Page'
    class Meta:
        verbose_name_plural = 'Home Page'

class ServicePage(SeoMixin):

    def __str__(self):
        return 'Service Page'
    class Meta:
        verbose_name_plural = 'Service Page'

class ContactPage(SeoMixin):
    def __str__(self):
        return 'Contact Page'
    class Meta:
        verbose_name_plural = 'Contact Page'

class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.name)
    class Meta:
        verbose_name_plural = 'Services'




class SiteSettings(models.Model):
    company_name = models.CharField(max_length=100, null=True, blank=True)
    logo_navbar = models.FileField(upload_to='core/site_settings',
                                   null=True, blank=True)

    logo_navbar_alt_data = models.CharField(max_length=255, null=True, blank=True,
                                            help_text='Add data for increasing SEO performance')

    logo_footer = models.FileField(upload_to='core/site_settings',
                                   null=True, blank=True)

    logo_footer_alt_data = models.CharField(max_length=255, null=True, blank=True,
                                            help_text='Add data for increasing SEO performance')

    favicon = models.FileField(upload_to='core/site_settings', null=True, blank=True)
    favicon_alt_data = models.CharField(max_length=255, null=True, blank=True,
                                        help_text='Add data for increasing SEO performance')

    address = models.CharField(max_length=255, null=True, blank=False)
    longitude = models.DecimalField(max_digits=17, decimal_places=15, null=True, blank=False)
    latitude = models.DecimalField(max_digits=17, decimal_places=15, null=True, blank=False)
    iframe = models.TextField(help_text="Just paste iframe src data from googlemap")
    email = models.EmailField()
    phone_number = models.CharField(max_length=255, null=True, blank=False,
                                    help_text='Enter phone number starting with the code')

    fax = models.CharField(max_length=255, null=True, blank=False,
                                    help_text='Enter fax number starting with the code')

    facebook = models.URLField(max_length=255, null=True, blank=True, help_text='Enter your facebook url')
    instagram = models.URLField(max_length=255, null=True, blank=True, help_text='Enter your instagram url')
    twitter = models.URLField(max_length=255, null=True, blank=True, help_text='Enter your twitter url')
    linkedin = models.URLField(max_length=255, null=True, blank=True, help_text='Enter your linkedin url')
    youtube = models.URLField(max_length=255, null=True, blank=True, help_text='Enter your youtube url')


    def __str__(self):
        return 'Site Settings'

    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Site Settings'