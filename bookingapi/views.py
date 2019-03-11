from rest_framework import generics
from booking_app.models import Booking
from . import  serializers

class BookingsList(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = serializers.BookingSerializer

class BookingsByUser(generics.ListAPIView):
    serializer_class = serializers.BookingSerializer
    def get_queryset(self):
        queryset = Booking.objects.all()
        user_id = self.kwargs['id']
        if user_id is not None:
            queryset = queryset.filter(user_id=user_id)
        return queryset
