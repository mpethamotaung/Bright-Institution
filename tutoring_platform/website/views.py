from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def booking(request):
    return render(request, 'booking.html', {})

def courses(request):
    return render(request, 'courses.html',{})

def pricing(request):
    return render(request, 'pricing.html',{})