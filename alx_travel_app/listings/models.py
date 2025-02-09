from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from uuid import uuid4

# Create your models here.
class Listing(models.Model):
    listing_id = models.UUIDField(primary_key=True, default=uuid4)
    host = models.ForeignKey('User', on_delete=models.CASCADE, db_column='host_id')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    location = models.CharField(max_length=50)
    pricepernight = models.DecimalField(decimal_places=2, max_digits=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Booking(models.Model):
    class BookingStatus(models.TextChoices):
        PENDING = 'pending', _('pending')
        CONFIRMED = 'confirmed', _('confirmed')
        CANCELED = 'canceled', _('canceled')


    booking_id = models.UUIDField(primary_key=True, default=uuid4)
    listing = models.ForeignKey('Listing', models.CASCADE, db_column='listing_id')
    user = models.ForeignKey('User', on_delete=models.CASCADE, db_column='user_id')
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(decimal_places=2, max_digits=8)
    status = models.CharField(max_length=15, choices=BookingStatus)
    created_at = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    review_id = models.UUIDField(primary_key=True, default=uuid4)
    listing = models.ForeignKey('Listing', models.CASCADE, db_column='listing_id')
    user = models.ForeignKey('User', on_delete=models.CASCADE, db_column='user_id')
    rating = models.IntegerField(validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
