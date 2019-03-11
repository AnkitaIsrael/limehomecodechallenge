from django.db import models

"""

Model for Hotel that contains all specifications of the property

:property_name: Name of the property
:property_city: Name of the property's city
:address: Address of the property
:petsAllowed: If the property allows pets
:pricePerNight: The price of the stay at the property per night
:averageRating: Average rating of the property
:wifiAvailability: If the property provides wifi
:parkingAvailability: If the property provides parking
:latitudeCoordinates: The latitude coordinates of the property
:longitudeCoordinates: The longitude coordinates of the property

"""

class Hotel(models.Model):
   property_name = models.CharField(max_length=250, verbose_name='Name of Hotel')
   property_city = models.CharField(max_length=250, verbose_name = 'City of Hotel', default="")
   address = models.CharField(max_length=255, verbose_name='Address of Hotel')
   petsAllowed = models.BooleanField(verbose_name='Pets Allowed')
   pricePerNight = models.FloatField(verbose_name='Price per night')
   averageRating = models.FloatField(verbose_name='Average Rating')
   wifiAvailability = models.BooleanField(verbose_name='Wifi Availability')
   parkingAvailability = models.BooleanField(verbose_name='Parking Availability')
   latitudeCoordinates = models.FloatField(verbose_name='Latitude Coordinates', default=0.0)
   longitudeCoordinates = models.FloatField(verbose_name='Longitude Coordinates', default=0.0)

   class Meta:
   		unique_together=('property_name','address','latitudeCoordinates','longitudeCoordinates')

   def __str__(self):
         return self.property_name