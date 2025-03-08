from django.shortcuts import render

from core import models
from core.models import ContactInfo


# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html', context={})

def project(request):
    context = {
        'projects': models.Project.objects.all(),
    }
    return render(request, 'project.html', context)

def services(request):
    return render(request, 'services.html', context={})

def contact(request):
    contact_info = ContactInfo.objects.first()
    context = {
        'contact_info': contact_info,
    }
    return render(request, 'contact.html', context)


