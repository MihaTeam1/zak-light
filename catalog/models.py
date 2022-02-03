from django.contrib.postgres.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.db import models

from slugify import slugify
import eav
import datetime as dt

class Product(models.Model):
	name = models.CharField(max_length=255, blank=False, null=False, verbose_name='Название')
	slug = models.SlugField(unique=True, blank=True, verbose_name='Слаг')
	article = models.CharField(max_length=255, blank=False, null=False, verbose_name='Артикул')
	price = models.PositiveIntegerField(blank=False, null=False, verbose_name='Цена')
	discount = models.FloatField(default=0, blank=True, verbose_name='Скидка', validators=[MaxValueValidator(1), MinValueValidator(0)])
	category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=False, verbose_name='Катеория')
	images = models.ManyToManyField('images.Image', through='images.Product_Images', verbose_name='Изображения')
	subCategory = models.ForeignKey('SubCategory', on_delete=models.SET_NULL, null=True,blank=False, verbose_name='Подкатегория')
	indexPageShow = models.BooleanField(default=False, null=False, blank=False, verbose_name='indexPageShow')
	count = models.IntegerField(default=0,null=False,blank=False, verbose_name='Количество')

	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'

	def __init__(self, *args, **kwargs):
		super(Product, self).__init__(*args, **kwargs)
		self.slug = slugify(self.name)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name)
		super(Product, self).save(*args, **kwargs)

	def __str__(self):
		return self.name

	def validateDiscount(self):
		if self.discount > 1 or self.discount < 0:
			raise ValidationError('Discount must be in 0-1 range')

eav.register(Product)

class Category(models.Model):
	name = models.CharField(max_length=255, blank=False, null=False, verbose_name='Название')
	name_plural = models.CharField(max_length=255, blank=False, null=False, verbose_name='Название мн.ч.')
	slug = models.SlugField(unique=True, verbose_name='Слаг')
	slug_plural = models.SlugField(unique=True, verbose_name='Слаг мн.ч.')
	images = models.ManyToManyField('images.Image', through='images.Category_Images', verbose_name='Изображения')
	subCategories = models.ManyToManyField('SubCategory', through='Category_SubCategory', verbose_name='Подкатегории')


	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

	def __init__(self, *args, **kwargs):
		super(Category, self).__init__(*args, **kwargs)
		self.slug = slugify(self.name)
		self.slug_plural = slugify(self.name_plural)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name)
		if not self.slug_plural:
			self.slug_plural = slugify(self.name_plural)
		super(Category, self).save(*args, **kwargs)

	def __str__(self):
		return self.name

class SubCategory(models.Model):
	name = models.CharField(max_length=255, blank=False, null=False, verbose_name='Название')
	name_plural = models.CharField(max_length=255,blank=False, null=False, verbose_name='Название мн.ч.')
	slug = models.SlugField(blank=True, verbose_name='Слаг')
	slug_plural = models.SlugField(blank=True, verbose_name='Слаг мн.ч.')
	categories = models.ManyToManyField('Category', through='Category_SubCategory', verbose_name='Категории')
	images = models.ManyToManyField('images.Image', through='images.SubCategory_Images', blank=True, verbose_name='Изображения')

	class Meta:
		verbose_name = 'Подкатегория'
		verbose_name_plural = 'Подкатегории'

	def __init__(self, *args, **kwargs):
		super(SubCategory, self).__init__(*args, **kwargs)
		self.slug = slugify(self.name)
		self.slug_plural = slugify(self.name_plural)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name)
		if not self.slug_plural:
			self.slug_plural = slugify(self.name_plural)
		super(SubCategory, self).save(*args, **kwargs)


	def __str__(self):
		return self.name

class Category_SubCategory(models.Model):
	categoryId = models.ForeignKey('Category', on_delete=models.CASCADE)
	subCategoryId = models.ForeignKey('SubCategory', on_delete=models.CASCADE)
