from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from .models import Hotel
from django.conf import settings


SEED_GENERATION_SECRET = settings.SEED_GENERATION_SECRET


def getHotelSeeds():
    data = [
        {
            "property_name": "Viridian Sword Resort & Spa",
            "address": "4711 White Pine Lane",
            "petsAllowed": True,
            "pricePerNight": 56.0,
            "averageRating": 3.5,
            "wifiAvailability": True,
            "parkingAvailability": False,
            "latitudeCoordinates":40.3984024,
            "longitudeCoordinates":-3.8350075},
        {
            "property_name": "Marina Aegis Resort & Spa",
            "address": "4801 Lonely Oak Drive",
            "petsAllowed": True,
            "pricePerNight": 52.0,
            "averageRating": 3.9,
            "wifiAvailability": True,
            "parkingAvailability": True,
            "latitudeCoordinates": 40.3984024 ,
            "longitudeCoordinates": -3.835007516},
        {
            "property_name": "Valeyrian Resort & Spa",
            "address": "4711 White Pine Lane",
            "petsAllowed": True,
            "pricePerNight": 56.0,
            "averageRating": 1.5,
            "wifiAvailability": True,
            "parkingAvailability": False,
            "latitudeCoordinates": 40.3984024,
            "longitudeCoordinates": -3.8350075},
        {
            "property_name": "Atlantic Resort & Spa",
            "address": "4711 White Pine Lane",
            "petsAllowed": True,
            "pricePerNight": 26.0,
            "averageRating": 3.4,
            "wifiAvailability": True,
            "parkingAvailability": False,
            "latitudeCoordinates": 40.3984024,
            "longitudeCoordinates": -3.8350075},
        {
            "property_name": "Sword Resort & Spa",
            "address": "4711 White Pine Lane",
            "petsAllowed": True,
            "pricePerNight": 56.0,
            "averageRating": 3.5,
            "wifiAvailability": False,
            "parkingAvailability": False,
            "latitudeCoordinates": 40.3984024,
            "longitudeCoordinates": -3.8350075},
        {
            "property_name": "Ana Mareno Resort & Spa",
            "address": "4711 White Pine Lane",
            "petsAllowed": True,
            "pricePerNight": 99.0,
            "averageRating": 2.5,
            "wifiAvailability": True,
            "parkingAvailability": True,
            "latitudeCoordinates": 40.3984024,
            "longitudeCoordinates": -3.8350075},
        {
            "property_name": "Imdea Resort & Spa",
            "address": "4711 White Pine Lane",
            "petsAllowed": True,
            "pricePerNight": 56.0,
            "averageRating": 2.5,
            "wifiAvailability": True,
            "parkingAvailability": False,
            "latitudeCoordinates": 40.3984024,
            "longitudeCoordinates": -3.8350075},
        {
            "property_name": "Accent Resort & Spa",
            "address": "4711 White Pine Lane",
            "petsAllowed": True,
            "pricePerNight": 78.0,
            "averageRating": 3.2,
            "wifiAvailability": False,
            "parkingAvailability": False,
            "latitudeCoordinates": 40.3984024,
            "longitudeCoordinates": -3.8350075},
        {
            "property_name": "Melody Resort & Spa",
            "address": "4711 White Pine Lane",
            "petsAllowed": True,
            "pricePerNight": 34.0,
            "averageRating": 3.1,
            "wifiAvailability": True,
            "parkingAvailability": False,
            "latitudeCoordinates": 40.3984024,
            "longitudeCoordinates": -3.8350075},
        {
            "property_name": "Soft Sword Resort & Spa",
            "address": "4711 White Pine Lane",
            "petsAllowed": True,
            "pricePerNight": 90.0,
            "averageRating": 4.5,
            "wifiAvailability": True,
            "parkingAvailability": True,
            "latitudeCoordinates": 40.3984024,
            "longitudeCoordinates": -3.8350075},
    ]
    return data

# def getSeedGenerationAuthToken():

def runSeeds(request):
    authToken = request.GET.get('authToken', None)
    if authToken != SEED_GENERATION_SECRET:
        return HttpResponse('[401] Unauthorized', status=401)

    seedData = getHotelSeeds()
    for seedObject in seedData:
        hotelInstance, created = Hotel.objects.get_or_create(
            property_name=seedObject["property_name"],
            address=seedObject["address"],
            petsAllowed=seedObject["petsAllowed"],
            pricePerNight=seedObject["pricePerNight"],
            averageRating=seedObject["averageRating"],
            wifiAvailability=seedObject["wifiAvailability"],
            parkingAvailability = seedObject["parkingAvailability"],
            latitudeCoordinates = seedObject["latitudeCoordinates"],
            longitudeCoordinates = seedObject["longitudeCoordinates"]
        )
        if not created:
            hotelInstance.save()

    return HttpResponse("[200] Seed Generation Success!")


