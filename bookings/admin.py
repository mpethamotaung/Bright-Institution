from django.contrib import admin
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ['student', 'tutor', 'date', 'time', 'subject']
    list_filter = ['date', 'tutor']
    search_fields = ['student__user__username', 'tutor__user__username', 'subject']

admin.site.register(Booking, BookingAdmin)
