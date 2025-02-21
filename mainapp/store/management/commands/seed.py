from django.core.management.base import BaseCommand
from store.models import Product, Publisher
from faker import Faker
import random

fake = Faker()

class Command(BaseCommand):
    help = 'Seed database with test data'

    def handle(self, *args, **kwargs):
        
        publishers = [
            Publisher(name="Publisher 1"),
            Publisher(name="Publisher 2"),
        ]
        Publisher.objects.bulk_create(publishers)
        self.stdout.write(self.style.SUCCESS('Publishers added successfully!'))


        products = []
        
        
        for _ in range(10):
            product = Product(
                name=fake.word(),
                description=fake.text(),
                price=round(random.uniform(10, 1000), 2),
                pages=random.randint(50, 1000),
                publisher_id=random.randint(1, 5),
                language="en",
                cover_type="Hardcover",
                format="Paperback",
                weight=random.randint(200, 1500),
                year_published=random.randint(2000, 2025),
                isbn=fake.isbn13(),
            )
            products.append(product)

        Product.objects.bulk_create(products)
        
        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
