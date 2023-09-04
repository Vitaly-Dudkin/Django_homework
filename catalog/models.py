from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(verbose_name='description')
    image = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name='image')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='category')
    purchase_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='date_of_creation')
    last_modified_date = models.DateTimeField(auto_now=True, verbose_name='last_modified_date')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('last_modified_date', 'name',)


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    description = models.TextField(verbose_name='description')

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


class Version(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Product')
    version_number = models.PositiveSmallIntegerField(verbose_name='Number of version')
    version_name = models.CharField(max_length=100, verbose_name='Name of version')
    is_current = models.BooleanField(default=True, verbose_name='Active version')

    def __str__(self):
        return f"{self.version_name}: {self.version_number}, {self.is_current}"

    def save(self, *args, **kwargs):
        if self.is_current:
            Version.objects.filter(product=self.product, is_current=True).update(is_current=False)
        super(Version, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Version'
        verbose_name_plural = 'Versions'
