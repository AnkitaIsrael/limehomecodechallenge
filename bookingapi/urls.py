from django.urls import path, include

from . import views
#
urlpatterns = [
     path('all_bookings/', views.BookingsList.as_view(), name='bookings_list'),
]