from rest_framework import serializers
from .models import Listing, Booking, Review
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  # customize as needed



class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['listing_id', 'title', 'description', 'location', 'price']

class BookingSerializer(serializers.ModelSerializer):
    booked_by = serializers.StringRelatedField(read_only=True)  # Show username or user string
    listing = ListingSerializer(read_only=True)

    # Accept only listing_id from frontend when creating a booking
    listing_id = serializers.PrimaryKeyRelatedField(
        queryset=Listing.objects.all(), source='listing', write_only=True
    )

    class Meta:
        model = Booking
        fields = ['booking_id', 'booked_by', 'booking_date', 'listing', 'listing_id']
        read_only_fields = ['booking_date', 'booked_by']


class ReviewSerializer(serializers.ModelSerializer):
    listing = ListingSerializer(read_only=True)
    booking = BookingSerializer(read_only=True)

    # Accept IDs on input
    listing_id = serializers.PrimaryKeyRelatedField(
        queryset=Listing.objects.all(), source='listing', write_only=True)
    booking_id = serializers.PrimaryKeyRelatedField(
        queryset=Booking.objects.all(), source='booking', write_only=True)

    class Meta:
        model = Review
        fields = ['review_id', 'listing', 'booking', 'created_at', 'comment', 'review_rating', 'listing_id', 'booking_id']
        read_only_fields = ['created_at']