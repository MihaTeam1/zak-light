from django import forms
from django.db import models
from django.contrib import admin

from eav.forms import BaseDynamicEntityForm

from catalog.models import *

class ProductForm(BaseDynamicEntityForm):
	model = Product
	class Meta:
		fields = [
			'name',
			'price',
			'discount',
			'category',
			'subCategory',
		]

class CategoryForm(forms.ModelForm):
	model = Category
	class Meta:
		exclude = ['slug', 'slug_plural']

class SubCategoryForm(forms.ModelForm):
	model = SubCategory
	class Meta:
		exclude = ['slug', 'slug_plural']