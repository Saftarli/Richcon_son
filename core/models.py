from django.db import models

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

