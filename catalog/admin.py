from django.contrib import admin
from eav.admin import BaseEntityAdmin
from catalog.models import *
from catalog.forms import *
from images.models import *
from images.admin import *
from images.forms import *

class CategoryInline(admin.TabularInline):
	model = Category_SubCategory
	form = CategoryForm

class SubCategoryInline(admin.TabularInline):
	model = Category_SubCategory
	form = SubCategoryForm

class ProductAdmin(BaseEntityAdmin):
	inlines = (Product_ImagesInline,)
	form = ProductForm

class BrandAdmin(admin.ModelAdmin):
	pass

class CategoryAdmin(admin.ModelAdmin):
	inlines = (Category_ImagesInline, SubCategoryInline,)
	model = Category
	form = CategoryForm

class SubCategoryAdmin(admin.ModelAdmin):
	inlines = (SubCategory_ImagesInline,CategoryInline,)
	model = SubCategory
	form = SubCategoryForm


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)

