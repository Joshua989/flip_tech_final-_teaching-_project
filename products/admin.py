from django.contrib import admin
from .models import Category, Product


@admin.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'stock', 'available', 'created_at', 'image']
    list_filter = ['available', 'category']
    list_editable = ['price', 'stock',  'available']
    prepopulated_fields = {'slug': ('name',)}





