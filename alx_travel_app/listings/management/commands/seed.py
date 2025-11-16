from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        # Sample data
        sample_listings = [
            {
                "title": "Cozy Apartment in NYC",
                "description": "A lovely apartment near Central Park.",
                "price_per_night": 120.00,
                "location": "New York, NY"
            },
            {
                "title": "Beachfront Villa",
                "description": "Luxury villa with stunning ocean views.",
                "price_per_night": 350.00,
                "location": "Malibu, CA"
            },
            {
                "title": "Mountain Cabin Retreat",
                "description": "Escape to the mountains in this peaceful cabin.",
                "price_per_night": 200.00,
                "location": "Aspen, CO"
            },
        ]

        # Clear existing listings
        Listing.objects.all().delete()

        # Create new listings
        for listing_data in sample_listings:
            Listing.objects.create(**listing_data)

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
