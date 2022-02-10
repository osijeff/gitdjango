from django.contrib import admin
from  .models import Category, Product

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_field = {'slug': ('name')}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'image', 'category', 'availability', 'slug')
    list_filter = ['availability']
    list_editable = ('price', 'availability')
    search_field = ('name', 'category', 'availability')
    prepopulated_field = {'slug': ('name')}