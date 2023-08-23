from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name='изображение')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория')
    purchase_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    last_modified_date = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('last_modified_date', 'name',)


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('name',)


class BlogPost(models.Model):
    title = models.CharField(max_length=255, verbose_name='header')
    slug = models.CharField(max_length=255, unique=True, verbose_name='slug')
    content = models.TextField(null=True, blank=True, verbose_name='content')
    preview = models.ImageField(upload_to='catalog/', null=True, blank=True, verbose_name='image')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='date_of_creation')
    is_published = models.BooleanField(default=True, verbose_name='published')
    views_count = models.IntegerField(default=0, verbose_name='count_of_views')

    def __str__(self):
        return f'{self.title, self.views_count}'

    class Meta:
        verbose_name = 'Publication'
        verbose_name_plural = 'Publications'
