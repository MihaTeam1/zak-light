from django import forms
from django.db import models
from images.models import *

class ImageForm(forms.ModelForm):
	model = Image

class Product_ImagesForm(forms.ModelForm):
	model = Product_Images

class Category_ImagesForm(forms.ModelForm):
	model = Category_Images

class SubCategory_ImagesForm(forms.ModelForm):
	model = SubCategory_Images

