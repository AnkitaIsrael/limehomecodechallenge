from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from .models import Customer
from django.contrib.auth.models import User

from django.conf import settings


SEED_GENERATION_SECRET = settings.SEED_GENERATION_SECRET


def getCustomerSeeds():
    data = [
        {
            "forename": "Soheil",
            "surname": "Gabunia",
            "email": "soheil@gmail.com",
            "password": "ankita123456",
            "phone": 4567890987,
            "address": "USCGC Miller FPO AA 39410",
            "country": "USA"},
        {
            "forename": "Ankita",
            "surname": "Sadu",
            "email": "ankita@gmail.com",
            "password": "ankita123456",
            "phone": 34567654323,
            "address": "14250 Lang Common Suite 104 Harrisonfurt, UT 88378",
            "country": "India"},
        {
            "forename": "Giorgi",
            "surname": "Capir",
            "email": "giorgi@gmail.com",
            "password": "ankita123456",
            "phone": 1234565432,
            "address": "62654 Drake Crescent Suite 908 New Heatherburgh, AK 96663",
            "country": "Pakistan"},
        {
            "forename": "Lucas",
            "surname": "Lukir",
            "email": "lucas@gmail.com",
            "password": "ankita123456",
            "phone": 6655676457,
            "address": "USNV Gilmore FPO AP 64869",
            "country": "Argentina"},
        {
            "forename": "Daniel",
            "surname": "Tounic",
            "email": "daniel@gmail.com",
            "password": "ankita123456",
            "phone": 63738483749,
            "address": "63405 Berry Pines Suite 848 Karenport, WY 06449",
            "country": "Romania"},
        {
            "forename": "Sabina",
            "surname": "Fekir",
            "email": "sabina@gmail.com",
            "password": "ankita123456",
            "phone": 6348583648,
            "address": "57722 Sherri Loaf North Christine, OH 66577",
            "country": "Bangladesh"},
        {
            "forename": "Luis",
            "surname": "Miguel",
            "email": "luis@gmail.com",
            "password": "ankita123456",
            "phone": 8097498573,
            "address": "Unit 7613 Box 5227 DPO AE 68080",
            "country": "USA"},
        {
            "forename": "Vatsan",
            "surname": "Kundarani",
            "email": "vatson@gmail.com",
            "password": "ankita123456",
            "phone": 376473649264,
            "address": "5035 April Junction Suite 412 New Nicoleside, VT 46677",
            "country": "Manchester"},
        {
            "forename": "Salomi",
            "surname": "Sadi",
            "email": "salomi@gmail.com",
            "password": "ankita123456",
            "phone": 66733638323,
            "address": "313 Chapman Square South Amyview, MN 87441",
            "country": "York"},
        {
            "forename": "Felipe",
            "surname": "Feda",
            "email": "Felipe@gmail.com",
            "password": "ankita123456",
            "phone": 73883784672,
            "address": "323 Alexandria Glens Apt. 722 Munozland, PA 86833",
            "country": "Uganda"}
    ]
    return data

# def getSeedGenerationAuthToken():

def runSeeds(request):
    authToken = request.GET.get('authToken', None)
    if authToken != SEED_GENERATION_SECRET:
        return HttpResponse('[401] Unauthorized', status=401)

    seedData = getCustomerSeeds()
    for seedObject in seedData:
        user = User.objects.create_user(username=seedObject["email"])
        user.set_password(seedObject["password"])
        user.save()
        customerInstance, created = Customer.objects.get_or_create(user=user, defaults={
            "forename":seedObject["forename"],
            "surname":seedObject["surname"],
            "phone":seedObject["phone"],
            "address":seedObject["address"],
            "country":seedObject["country"]}
            )
        if created:
            customerInstance.save()

    return HttpResponse("[200] Seed Generation Success!")


