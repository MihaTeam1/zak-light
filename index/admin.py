from django.contrib import admin

from index.forms import *
from index.models import *

class SiteConfigurationAdmin(admin.ModelAdmin):
	form = SiteConfigurationForm
	model = SiteConfiguration

class ContactAdmin(admin.ModelAdmin):
	form = ContactForm
	model = ContactModel

admin.site.register(SiteConfiguration, SiteConfigurationAdmin)
admin.site.register(ContactModel, ContactAdmin)
