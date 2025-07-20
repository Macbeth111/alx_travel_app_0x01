from django.db import models
from django.utils import timezone


class Listing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Booking(models.Model):
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name='bookings')
    guest_name = models.CharField(max_length=100)
    guest_email = models.EmailField()
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"Booking by {self.guest_name} for {self.listing.title}"


class Review(models.Model):
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name='reviews')
    reviewer_name = models.CharField(max_length=100)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Review by {self.reviewer_name} for {self.listing.title}"
