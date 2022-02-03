from django import forms
from django.db import models
from django.contrib import admin

from index.models import *

class SiteConfigurationForm(forms.ModelForm):
	model = SiteConfiguration

class ContactForm(forms.ModelForm):
	model = ContactModel