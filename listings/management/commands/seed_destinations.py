from django.core.management.base import BaseCommand
from listings.models import TravelDestination


class Command(BaseCommand):
    help = 'Seeds the database with travel destinations'

    def handle(self, *args, **kwargs):
        destinations = [
            {
                'name': 'Safari Adventure',
                'description': 'Experience the wild savannah and majestic wildlife.',
                'location': 'Serengeti, Tanzania',
                'price': 1500.00,
                'available': True
            },
            {
                'name': 'Beach Paradise',
                'description': 'Relax on white sandy beaches with clear blue waters.',
                'location': 'Zanzibar, Tanzania',
                'price': 900.00,
                'available': True
            },
            {
                'name': 'Mountain Escape',
                'description': 'Hike through the lush mountains and enjoy nature.',
                'location': 'Rwenzori Mountains, Uganda',
                'price': 1200.00,
                'available': False
            },
        ]

        for data in destinations:
            obj, created = TravelDestination.objects.get_or_create(**data)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Added: {obj.name}"))
            else:
                self.stdout.write(self.style.WARNING(
                    f"Already exists: {obj.name}"))
