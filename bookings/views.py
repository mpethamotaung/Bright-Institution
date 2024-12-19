from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Booking

@login_required
def create_booking(request):
    if request.user.is_student:
        if request.method == 'POST':
            form = BookingForm(request.POST, student=request.user.student_profile)
            if form.is_valid():
                booking = form.save(commit=False)
                booking.student = request.user.student_profile
                booking.save()
                return redirect('bookings:booking_list')
        else:
            form = BookingForm(student=request.user.student_profile)
    else:
        form = None

    return render(request, 'bookings/create_booking.html', {'form': form})

@login_required
def booking_list(request):
    if request.user.is_student:
        bookings = request.user.student_profile.bookings.all()
    elif request.user.is_tutor:
        bookings = request.user.tutor_profile.bookings.all()
    else:
        bookings = []

    return render(request, 'bookings/booking_list.html', {'bookings': bookings})
