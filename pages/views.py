from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def booking(request):
    return render(request, 'pages/booking.html')

def courses(request):
    return render(request, 'pages/courses.html')

def pricing(request):
    return render(request, 'pages/pricing.html')
