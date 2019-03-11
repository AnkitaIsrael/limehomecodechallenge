from django.db import models
from django.contrib.auth.models import User
from hotel_app.models import Hotel
import datetime

"""

Model for bookings that gets both the foreign keys from Customer and Hotel and has start and end dates for booking.

:user: Foreign key referencing Django's User Model
:hotel: Foreign key referencing Hotel Model
:dateFrom: Booking start date 
:dateTo: Booking end date

"""


class Booking(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', default= " ")
    hotel= models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel',  default= " ")
    dateFrom = models.DateField(verbose_name='Booking date from', default=datetime.date.today)
    dateTo = models.DateField(verbose_name='Booking date to', default = datetime.date.today)

    def __str__(self):
        return "#{3} hotel {0}, from {1} to {2}".format(self.hotel.property_name, self.dateFrom, self.dateTo, self.pk)
