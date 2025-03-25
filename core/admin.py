from django.contrib import admin
from core.models import *

class SingleInstanceAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return True

class HomePageAdmin(SingleInstanceAdmin):
    pass

class ServicePageAdmin(SingleInstanceAdmin):
    pass

class ContactPageAdmin(SingleInstanceAdmin):
    pass

class SiteSettingsAdmin(SingleInstanceAdmin):
    pass


admin.site.register(ContactInfo)
admin.site.register(Project)
admin.site.register(Employee)
admin.site.register(ServicePage, ServicePageAdmin)
admin.site.register(HomePage, HomePageAdmin)
admin.site.register(Service)
admin.site.register(ContactPage, ContactPageAdmin)
admin.site.register(SiteSettings, SiteSettingsAdmin)
