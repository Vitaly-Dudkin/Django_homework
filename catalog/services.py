from django.core.cache import cache

from catalog.models import Category
from django.conf import settings


def get_categories_from_cache():
    if settings.CACHE_ENABLED:
        key = 'categories'
        cache_data = cache.get(key)
        if cache_data is None:
            cache_data = Category.objects.all()
            cache.set(key, cache_data)
    else:

        cache_data = Category.objects.all()

    return cache_data
