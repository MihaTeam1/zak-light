from django.db import models
from django.utils.safestring import mark_safe

class Image(models.Model):
	image = models.ImageField(upload_to='images')

	class Meta:
		verbose_name = "Изображение"
		verbose_name_plural = "Изображения"

	def image_tag(self):
		return mark_safe('<img src="%s" style="max-width: 70px; max-height:70px;" />' % self.image.url)
	def image_tag_big(self):
		return mark_safe('<a href="{0}" target="_blank"><img src="{0}" style="max-width: min(600px, 100%); max-height:min(600px, 100%);" /></a>'.format(self.image.url))
	image_tag_big.short_description = 'Изображение'
	image_tag.allow_tags = True
	image_tag.short_description = 'Изобоажение'
	image_tag.allow_tags = True

	def __str__(self):
		return str(self.image.url).split('/')[-1]

class Product_Images(models.Model):
	imageId = models.ForeignKey('Image', on_delete=models.CASCADE)
	productId = models.ForeignKey('catalog.Product', on_delete=models.CASCADE)

class Category_Images(models.Model):
	imageId = models.ForeignKey('Image', on_delete=models.CASCADE)
	categoryId = models.ForeignKey('catalog.Category', on_delete=models.CASCADE)

class SubCategory_Images(models.Model):
	imageId = models.ForeignKey('Image', on_delete=models.CASCADE)
	subCategoryId = models.ForeignKey('catalog.SubCategory', on_delete=models.CASCADE)