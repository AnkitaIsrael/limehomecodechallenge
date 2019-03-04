from django.db import models

# Model for Customer that contains personal details
class Customer(models.Model):
   forename = models.CharField(max_length=20, verbose_name='First Name', default='')
   surname = models.CharField(max_length=20, verbose_name='Last Name', default='')
   email = models.EmailField(verbose_name='Email')
   phone = models.IntegerField(verbose_name='Phone', default=0)
   address = models.CharField(max_length=256, verbose_name='Home Address', default='')
   country = models.CharField(max_length=256, verbose_name='Country',default='')

