from faker import Faker
from customer_app.models import Customer

fakeGenerate = Faker()

def add_users(n):
    for i in range(0,n):
        fname = fakeGenerate.first_name()
        lname = fakeGenerate.last_name()
        email = fakeGenerate.email()
        phone = fakeGenerate.phone_number()
        addr = fakeGenerate.address()
        country= fakeGenerate.country()
        Customer(forename = fname, lastname = lname, email = email, address = addr, phone = phone, country= country)

