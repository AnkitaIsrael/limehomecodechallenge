from django.db import models
from customer_app.models import Customer
from hotel_app.models import Hotel

# Model for bookings that gets both the foreign keys from Customer and Hotel
class Booking(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer')
    hotel= models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel')

    class Meta:
        unique_together = ('customer', 'hotel')
