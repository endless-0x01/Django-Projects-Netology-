import csv
from decimal import Decimal

from django.core.management.base import BaseCommand
from phones.models import Phone
from datetime import date, datetime


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # TODO: Добавьте сохранение модели
            phone_id = int(phone['id'])
            name = phone['name'].strip()
            price = Decimal(phone['price'])
            image = phone['image'].strip()
            release_date = date.fromisoformat(phone['release_date'])
            lte_exists = phone['lte_exists'].lower() == 'true'

            try:
                Phone.objects.create(
                    id=phone_id,
                    name=name,
                    price=price,
                    image=image,
                    release_date=release_date,
                    lte_exists=lte_exists,
                )
            except Exception as e:
                print(f'Ошибка для телефона {name}, тип ошибки {type(e).__name__}: {e}')


