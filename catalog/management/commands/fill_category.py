import json

from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('data.json', 'r', encoding='utf-8') as file:
            lst = [Category(**kwargs['fields']) for kwargs in json.load(file)]
        self.delete_data()
        Category.objects.bulk_create(lst)


    def delete_data(self):
        Category.objects.all().delete()
