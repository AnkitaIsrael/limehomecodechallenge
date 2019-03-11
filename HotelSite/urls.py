"""HotelSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('bookingapi.urls')),
    path('', views.index),
    url(r'^hotel/', include(('hotel_app.urls', 'hotel_app'), namespace='hotelApp')),
    url(r'^booking/(?P<id>\d+)/$', views.bookingDetails, name="bookingDetails"),
    url(r'^book/(?P<id>\d+)/$', views.addBooking, name="addBooking"),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
]
