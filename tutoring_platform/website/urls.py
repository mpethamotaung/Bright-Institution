from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('booking.html', views.booking, name='booking'),
    path('courses.html', views.courses, name='courses'),
    path('pricing.html', views.pricing, name='pricing'),
    path('resources.html', views.resources, name='resources'),
    path('signup.html', views.signup, name='signup'),
    path('student_profile.html', views.student_profile, name='student_profile'),
    path('tutor_profile.html', views.tutor_profile, name='tutor_profile'),
    path('tutors.html', views.tutors, name='tutors'),

]