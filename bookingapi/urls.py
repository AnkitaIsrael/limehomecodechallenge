from django.urls import path
from . import views
urlpatterns = [
     path('all_bookings/', views.BookingsList.as_view(), name='bookings_list'),
     path('bookingbyuser/<int:id>', views.BookingsByUser.as_view()),
]