from django.db import models

# Model for Customer that contains personal details
class Customer(models.Model):
    forename = models.CharField(max_length=20, verbose_name='First Name')
    surname = models.CharField(max_length=20, verbose_name='Last Name')
    email = models.EmailField(max_length=254, verbose_name='Email')
    phone = models.CharField(max_length=256, verbose_name='Phone')
    firstStreet = models.CharField(max_length=265, verbose_name='Street 1')
    secondStreet = models.CharField(max_length=256, verbose_name='Street 2')
    zipCode = models.CharField(max_length=256, verbose_name='ZIP/Postal Code')
