from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help = 'Populate products table with 10 entries'

    def handle(self, *args, **kwargs):
        for i in range(10):
            Product.objects.create(
                name=f'Product {i}',
                description=f'Description for Product {i}',
                thumbnail_url=f'https://example.com/thumbnail_{i}.jpg',
                origin_price=1000 + i * 100,
                discounted_price=800 + i * 100,
                discounted_rate=0.2,
                status='Active',
                in_stock=True if i % 2 == 0 else False,
                is_preorder=False,
                is_purchasable=True,
                delivery_condition='Standard',
                delivery_display=f'Delivery information for Product {i}',
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated the products table'))
