from django.shortcuts import render
from .models import Hotel

# Gets all properties from Hotels and references the main html page that shows list of hotels
def index(request):
    allHotels = Hotel.objects.all()
    context = {'allHotels': allHotels}
    return render(request, "index.html", context)

