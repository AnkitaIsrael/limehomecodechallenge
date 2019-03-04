# from faker import Faker
# from customer_app.models import Customer
# from hotel_app.models import Hotel
#
# fakeGenerate = Faker()
#
# def add_users(n):
#    for i in range(n):
#        fname = fakeGenerate.first_name()
#        lname = fakeGenerate.last_name()
#        email = fakeGenerate.email()
#        phone = fakeGenerate.phone_number()
#        addr = fakeGenerate.address()
#        country= fakeGenerate.countrpyty()
#        customerInstance = Customer.objects.create(forename = fname, lastname = lname, email = email, address = addr, phone = phone, country= country)
#        customerInstance.save()
#
# def add_hotels(n):
#     for i in range(n):
#         nameofHotel = fakeGenerate.first_name()
#         addressOfHotel = fakeGenerate.address()
#         isPetsAllowed = fakeGenerate.boolean(chance_of_getting_true=50)
#         pricePerNight = fakeGenerate.random_int(min=0, max=200)
#         averageRating = fakeGenerate.random_int(min=1, max=5)
#         wifiAvailability = fakeGenerate.boolean(chance_of_getting_true=50)
#         parkingAvailability = fakeGenerate.boolean(chance_of_getting_true=50)
#         latitude = fakeGenerate.latitude()
#         longitude = fakeGenerate.longitude()
#         hotel = Hotel.objects.create(property_name=nameofHotel, address=addressOfHotel, petsAllowed=isPetsAllowed, pricePerNight=pricePerNight,
#               averageRating= averageRating, wifiAvailability=wifiAvailability, parkingAvailability=parkingAvailability,
#               latitudeCoordinates=latitude, longitudeCoordinates=longitude)
#         hotel.save()
#
# # n = 100
# # add_hotels(n)
# # add_users(n)


import os
import time
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

cmd = 'python3 manage.py seed %s --number=%s'


def generateHotel(number):
    global cmd
    _app_name = "hotel_app"
    command = cmd%(_app_name, number)
    os.chdir(BASE_DIR)
    os.system(command)
    time.sleep(1)

def generateCustomer(number):
    global cmd
    _app_name = "customer_app"
    command = cmd%(_app_name, number)
    os.chdir(BASE_DIR)
    os.system(command)
    time.sleep(1)

def main():
    n = 10
    generateHotel(n)
    generateCustomer(n)

if __name__ == "__main__":
    main()