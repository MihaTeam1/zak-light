from django.db import models
from tinymce.models import HTMLField

class SiteConfiguration(models.Model):
	name = models.CharField(max_length=255, blank=False, null=False, verbose_name='Название')
	email = models.EmailField(null=True, blank=True)
	phone = models.CharField(max_length=11, null=True,blank=True)
	indexPageMsg = HTMLField(null=True,blank=True)
	indexMainteinMsg = HTMLField(null=True,blank=True)

	def save(self, *args, **kwargs):
		if not self.pk and SiteConfiguration.objects.exists():
			raise ValidationError('There is can be only one SiteConfiguration instance')
		return super(SiteConfiguration, self).save(*args, **kwargs)

class ContactModel(models.Model):
	name = models.CharField(max_length=255, blank=False, null=False, verbose_name='Имя')
	phone = models.CharField(max_length=11, null=False,blank=False)
	Msg = models.TextField(null=False,blank=False)