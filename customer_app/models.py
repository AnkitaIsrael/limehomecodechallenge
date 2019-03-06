from django.db import models
from django.contrib.auth.models import User

# Model for Customer that contains personal details
class Customer(models.Model):
   forename = models.CharField(max_length=20, verbose_name='First Name', default='')
   surname = models.CharField(max_length=20, verbose_name='Last Name', default='')
   # email = models.EmailField(verbose_name='Email')
   phone = models.IntegerField(verbose_name='Phone', default=0)
   address = models.CharField(max_length=256, verbose_name='Home Address', default='')
   country = models.CharField(max_length=256, verbose_name='Country',default='')
   user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='customer') # only use username as email and password field


   def __unicode__(self):
   		return "[" + self.user.username + "]: " + self.forename + " "+ self.surname

   def __str__(self):
   		return "[" + self.user.username + "]: " + self.forename + " "+ self.surname