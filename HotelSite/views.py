import random

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
import sys
import math
import geocoder
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from hotel_app.models import Hotel
from booking_app.models import Booking

from django.template.context_processors import csrf


# Find the ip address of the user to get Latitude and longitude
g = geocoder.ip('me')

def update_hotel_coordinates():

    # Choose your the radius and convert to degrees
    radius = 17000
    radiusInDegrees = radius / 111300
    r = radiusInDegrees

    #Get the latitude and longitude coordinates
    x0 = g.latlng[0]
    y0 = g.latlng[1]

    #Go through all the hotel objects and update the coordinates of Latitude and Longitude fields
    hotels = Hotel.objects.all()
    for hotel in hotels:
        u = float(random.uniform(0.0, 1.0))
        v = float(random.uniform(0.0, 1.0))
        w = r * math.sqrt(u)
        t = 2 * math.pi * v
        x = w * math.cos(t)
        y = w * math.sin(t)
        xLat = x + x0
        yLong = y + y0
        hotel.latitudeCoordinates=float(xLat)
        hotel.longitudeCoordinates=float(yLong)
        hotel.save()
    return True

def update_hotel_city():
    hotels = Hotel.objects.all()
    for hotel in hotels:
        hotel.property_city = g.city
        hotel.save()

# Gets all properties from Hotels and references the main html page that shows list of hotels
def index(request):
    update_hotel_coordinates()
    update_hotel_city()
    allHotels = Hotel.objects.all()
    context = {'allHotels': allHotels}
    return render(request, "index.html", context)


def bookingDetails(request, id):
    hotelDetail = Hotel.objects.get(id=id)
    context = {
        'hotelDetail' : hotelDetail
    }

    return render(request, "booking.html", context)

def addBooking(request, id):
    if request.method=='POST':
        startDate = request.POST.get("booking-start")
        endDate = request.POST.get("booking-end")
        hotelDetail = Hotel.objects.get(id=id)
        current_user= User.objects.get(id=request.user.id)
        new_booking = Booking(user=current_user, hotel=hotelDetail, dateFrom=startDate, dateTo=endDate)
        new_booking.save()
        return render(request, "booking.html", {'hotel':hotelDetail})

    if request.method == 'GET':
        hotelDetail = Hotel.objects.get(id=id)
        return render(request, "selectDates.html", {'hotel':hotelDetail})






