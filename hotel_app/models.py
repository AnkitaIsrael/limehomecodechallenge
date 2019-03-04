from django.db import models

#Model for Hotel that contains all specifications of the property
class Hotel(models.Model):
   property_name = models.CharField(max_length=250, verbose_name='Name of Hotel')
   address = models.CharField(max_length=255, verbose_name='Address of Hotel')
   petsAllowed = models.BooleanField(verbose_name='Pets Allowed')
   pricePerNight = models.FloatField(verbose_name='Price per night')
   averageRating = models.FloatField(verbose_name='Average Rating')
   wifiAvailability = models.BooleanField(verbose_name='Wifi Availability')
   parkingAvailability = models.BooleanField(verbose_name='Parking Availability')
   latitudeCoordinates = models.FloatField(verbose_name='Latitude Coordinates', default=0.0)
   longitudeCoordinates = models.FloatField(verbose_name='Longitude Coordinates', default=0.0)





