from django.shortcuts import render
from catalog.models import *
from index.models import *
from index.forms import *
from django.template import Template, RequestContext
from django.conf import settings

def getIndexPage(request):
	products = Product.objects.prefetch_related().all()[:8]
	configuration = SiteConfiguration.objects.get(pk=1)
	context = {
		'products': products,
		'phoneReadeble': '+{0} {1}{2}{3} {4}{5}{6}-{7}{8}-{9}{10}'.format(*[char for char in configuration.phone]),
		'phoneRaw': '+' + configuration.phone,
		'configuration': configuration,
		'MEDIA_URL': settings.MEDIA_URL,
	}
	return render(request, 'index.html', context)

def getMaintenancePage(request):
	configuration = SiteConfiguration.objects.get(pk=1)
	context = {
		'phoneReadeble': '+{0} {1}{2}{3} {4}{5}{6}-{7}{8}-{9}{10}'.format(*[char for char in configuration.phone]),
		'phoneRaw': '+' + configuration.phone,
		'configuration': configuration,
		'MEDIA_URL': settings.MEDIA_URL,
	}
	return render(request, 'maintenance.html', context)
