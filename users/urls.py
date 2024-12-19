from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup_selection, student_signup, tutor_signup, profile, dashboard, tutor_dashboard, student_dashboard

app_name = 'users'

urlpatterns = [
    path('signup/selection/', signup_selection, name='signup_selection'),
    path('signup/student/', student_signup, name='student_signup'),
    path('signup/tutor/', tutor_signup, name='tutor_signup'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('profile/', profile, name='profile'),
    path('profile/update/', profile, name='update_profile'),  # Add this line for updating profile
    path('dashboard/', dashboard, name='dashboard'),  # Redirect based on user role
    path('tutor-dashboard/', tutor_dashboard, name='tutor_dashboard'),  # Tutor-specific dashboard
    path('student-dashboard/', student_dashboard, name='student_dashboard'),  # Student-specific dashboard
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
