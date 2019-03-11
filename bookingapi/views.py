from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from booking_app.models import Booking
from . import  serializers
import json


class BookingsList(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = serializers.BookingSerializer

def getUserBookings(request):
    if not request.user.is_authenticated():
        return HttpResponse("[400] Access Denied")

def getUserBookings(request):
        if not request.user.is_authenticated():
            return HttpResponse("[400] Access Denied")

        userBookings = Booking.objects.filter(user=request.user).get()

        serialized_obj = serializers.serialize('json', [userBookings, ])

        struct = json.loads(serialized_obj)
        data = json.dumps(struct[0])
        return HttpResponse(data, mimetype='application/json')

