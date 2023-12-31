from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'purchase_price',
        'category',

    )
    list_filter = ('category',)
    search_fields = ('name', 'description')
    ordering = ('pk',)


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)
    ordering = ('pk',)


@admin.register(BlogPost)
class BlogPost(admin.ModelAdmin):
    list_display = ('id', 'title', 'views_count')
    search_fields = ('title',)
    ordering = ('pk',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'version_number', 'version_name', 'is_current')
    search_fields = ('product',)
    list_filter = ('is_current', 'product',)
