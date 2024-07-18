from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def booking(request):
    return render(request, 'booking.html',{})

def courses(request):
    return render(request, 'courses.html',{})

def pricing(request):
    return render(request, 'pricing.html',{})

def resources(request):
    return render(request, 'resources.html',{})

def singup(request):
    return render(request, 'signup.html',{})

def student_profile(request):
    return render(request, 'student_profile.html',{})

def tutor_profile(request):
    return render(request, 'tutor_profile.html',{})

def tutors(request):
    return render(request, 'tutors.html',{})