from .models import Listing, Booking, User
from rest_framework import serializers

class ListingSerializer(serializers.ModelSerializer):
    host_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), pk_field=serializers.UUIDField(format='hex'))

    class Meta:
        model = Listing
        fields = ['listing_id', 'host_id', 'name', 'description', 'location', 'pricepernight', 'created_at', 'updated_at']

class BookingSerializer(serializers.ModelSerializer):
    listing_id = serializers.PrimaryKeyRelatedField(queryset=Listing.objects.all(), pk_field=serializers.UUIDField(format='hex'))
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), pk_field=serializers.UUIDField(format='hex'))
    class  Meta:
        model = Booking
        field = ['booking_id', 'listing_id', 'user_id', 'start_date', 'end_date', 'total_price', 'status', 'created_at']
