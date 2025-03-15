

import requests
from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help = 'Insert products from API'

    def handle(self, *args, **options):
        response = requests.get('https://fakestoreapi.com/products')

        if response.status_code == 200:
            data = response.json()

            for product in data:
                Product.objects.create(
                    name=product['title'],
                    price=product['price'],
                    description=product['description'],
                    image=product['image']
                )
            self.stdout.write(self.style.SUCCESS('Data inserted successfully'))
        else:
            self.stdout.write(self.style.ERROR('Error inserting data'))
            