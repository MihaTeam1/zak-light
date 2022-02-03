from django.contrib import admin
from catalog.models import *
from catalog.forms import *
from images.models import *
from images.forms import *



class Product_ImagesInline(admin.TabularInline):
	model = Product_Images
	form = Product_ImagesForm

class Category_ImagesInline(admin.TabularInline):
	model = Category_Images
	form = Category_ImagesForm

class SubCategory_ImagesInline(admin.TabularInline):
	model = SubCategory_Images
	form = SubCategory_ImagesForm

class Product_ImagesAdmin(admin.ModelAdmin):
	model = Product_Images
	form = Product_ImagesForm

class Category_ImagesAdmin(admin.ModelAdmin):
	model = Category_Images
	form = Category_ImagesForm

class SubCategory_ImagesAdmin(admin.ModelAdmin):
	model = SubCategory_Images
	form = SubCategory_ImagesForm

class ImageAdmin(admin.ModelAdmin):
	model = Image
	form = ImageForm
	list_display = ('image_tag',)
	fields = ('image_tag_big', 'image',)
	readonly_fields = ('image_tag_big',)

admin.site.register(Image, ImageAdmin)
admin.site.register(Product_Images, Product_ImagesAdmin)
admin.site.register(Category_Images, Category_ImagesAdmin)
admin.site.register(SubCategory_Images, SubCategory_ImagesAdmin)