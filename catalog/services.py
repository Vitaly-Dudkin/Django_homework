from django.core.cache import cache

from catalog.models import Category
from django.conf import settings


def get_categories_from_cache():
    queryset = Category.objects.all()
    if settings.CACHE_ENABLED:
        key = 'categories'
        cache_data = cache.get(key)
        if cache_data is None:
            cache_data = queryset
            cache.set(key, cache_data)

        return cache_data

    return queryset
