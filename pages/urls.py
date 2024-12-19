from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('booking/', views.booking, name='booking'),
    path('courses/', views.courses, name='courses'),
    path('pricing/', views.pricing, name='pricing'),
]
