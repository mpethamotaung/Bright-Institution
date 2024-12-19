from django.urls import path
from .views import create_booking, booking_list

app_name = 'bookings'

urlpatterns = [
    path('create/', create_booking, name='create_booking'),
    path('list/', booking_list, name='booking_list'),
]
