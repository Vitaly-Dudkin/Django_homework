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


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)

# 'Для моделей категории и продукта настройте отображение в административной панели.' \
# ' Для категорий выведите id и наименование в список отображения, а для продуктов выведите в список id,' \
# ' название, цену и категорию'
