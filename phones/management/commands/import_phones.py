import csv
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r', encoding='utf-8') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone_data in phones:
            phone_name = phone_data['name']
            phone_slug = phone_name.lower().replace(' ', '-')  # Генерация slug из имени
            phone_id = int(phone_data['id'])
            phone_price = float(phone_data['price'])
            phone_release_date = phone_data['release_date']
            phone_lte_exists = phone_data['lte_exists'].lower() == 'true'

            phone = Phone(
                id=phone_id,
                name=phone_name,
                image=phone_data['image'],
                price=phone_price,
                release_date=phone_release_date,
                lte_exists=phone_lte_exists,
                slug=phone_slug  # Используем сгенерированный slug
            )
            phone.save()
            self.stdout.write(self.style.SUCCESS(f'Успешно импортирован {phone}'))
