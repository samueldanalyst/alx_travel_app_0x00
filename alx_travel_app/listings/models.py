from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""
In listings/models.py, define Listing, Booking, and Review models based on the provided
"""

class Listing(models.Model):
    listing_id = models.AutoField(primary_key=True)
    lister = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        self.title

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    booked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now_add=True)  # Automatically set on creation
    listing = models.ForeignKey(Listing,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.listing.title} booked by {self.booked_by.username}"

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    listing = models.ForeignKey(Listing, models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=True)
    created_at = models.DateField(auto_now=True)
    comment = models.TextField()
    review_rating = models.IntegerField()

    def __str__(self):
        return f"review given by {self.booking.booked_by.username} to {self.listing.lister.username}"