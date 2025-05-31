# listings/management/commands/seed.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        # Optionally, clear existing listings first
        Listing.objects.all().delete()
        
        # Create or get a user to be the lister of the listings
        user, created = User.objects.get_or_create(username='sampleuser', defaults={'email': 'sampleuser@example.com'})
        if created:
            user.set_password('password123')  # You can set a password if you want
            user.save()

        # Sample data for listings
        sample_listings = [
            {
                'title': 'Cozy Apartment in Downtown',
                'description': 'A beautiful and cozy apartment right in the city center.',
                'location': 'New York',
                'price': 120.00,
            },
            {
                'title': 'Beach House with Ocean View',
                'description': 'Relax and enjoy the ocean breeze in this lovely beach house.',
                'location': 'California',
                'price': 250.00,
            },
            {
                'title': 'Mountain Cabin Retreat',
                'description': 'Escape to the mountains with this peaceful cabin getaway.',
                'location': 'Colorado',
                'price': 180.00,
            },
            {
                'title': 'Modern Studio Flat',
                'description': 'A modern and compact studio, perfect for singles or couples.',
                'location': 'San Francisco',
                'price': 150.00,
            },
        ]

        # Create listings in the database
        for listing_data in sample_listings:
            Listing.objects.create(
                lister=user,
                title=listing_data['title'],
                description=listing_data['description'],
                location=listing_data['location'],
                price=listing_data['price'],
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with sample listings.'))
