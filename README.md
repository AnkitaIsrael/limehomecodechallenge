## Goal 

An app that shows properties around a user location and the provision to book them.

The minimum requirements for the app are:
 - Make sure there's a list, which lets you see/find any property around your current location.
 - Make sure the user can select a specific property, and create a "fake" booking request.
 - Show the booking requests list with a public API.

Time given: 10 days  

### Clone the project
```
git clone https://github.com/AnkitaIsrael/propertybooking.git
```
 
## Functionality
This app lets a user register, login and select reservation dates to reserve a property. The properties are displayed as a list and are also displayed on a map. 

## Installing
### Install Python
https://www.python.org/downloads/

### Install pip
https://pip.pypa.io/en/stable/installing/

### Install dependencies
```
pip3 install Django djangorestframework geocoder django_seeds
```

### Running
#### A developement server
Just run this command:
```
python3 manage.py runserver
```

### Relevant URLS

- Admin: 127.0.0.1:8000/admin 
  - Login with:
    - Username: ankitaisrael
    - Password: ankita007

- Homepage(when asked for location, please click yes): 127.0.0.1:8000/

- Login: 127.0.0.1:8000/accounts/login/

- Signup: 127.0.0.1:8000/accounts/signup/

- Public API
  - Gets all bookings: 127.0.0.1:8000/api/all_bookings
  - Gets all bookings of a particular user: 127.0.0.1:8000/api/bookingbyuser/id_of_user*

*Replace 'id_of_user' as any user's id: Try ankitaisrael who has user id:12
 (or) Try lucas who has user id:13*
 
 ### Resources used:
 - Stackoverflow
 - Django documentation
 - Codepen
 - w3schools
 
