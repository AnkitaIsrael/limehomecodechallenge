from django.contrib.auth.models import User
from rest_framework import serializers, generics
from booking_app.models import Booking
from hotel_app.models import Hotel

# For the use of Public API
class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('id', 'property_name', 'property_city')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class BookingSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    hotel=HotelSerializer()
    class Meta:
        model = Booking
        fields = ('id', 'user', 'hotel')




