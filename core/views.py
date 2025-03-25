from django.shortcuts import render

from core import models
from core.models import ContactInfo, Project, Service, HomePage, ServicePage, ContactPage


# Create your views here.
def index(request):
    context = {
        'projects': Project.objects.all(),
        'services': Service.objects.all(),
        'homepage': HomePage.objects.last(),
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html', context={})

def project(request):
    context = {
        'projects': Project.objects.all(),
    }
    return render(request, 'project.html', context)

def services(request):

    return render(request, 'services.html', context={
        'service_page': ServicePage.objects.last(),
        'services': Service.objects.all()})

def contact(request):
    contact_info = ContactInfo.objects.first()
    context = {
        'contact_info': contact_info,
        'contact_page': ContactPage.objects.last(),
    }
    return render(request, 'contact.html', context)


