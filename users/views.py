from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from django.urls import reverse
from .forms import StudentSignupForm, TutorSignupForm, StudentProfileForm, TutorProfileForm, CustomUserChangeForm


# Student Signup View
@transaction.atomic
def student_signup(request):
    if request.method == 'POST':
        form = StudentSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful! Welcome to the platform.")
            return redirect('users:student_dashboard')
        else:
            messages.error(request, "There was an error with your form. Please check and try again.")
    else:
        form = StudentSignupForm()

    return render(request, 'users/signup_student.html', {'form': form})


# Tutor Signup View
@transaction.atomic
def tutor_signup(request):
    if request.method == 'POST':
        form = TutorSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful! Welcome to the platform.")
            return redirect('users:tutor_dashboard')
        else:
            messages.error(request, "There was an error with your form. Please check and try again.")
    else:
        form = TutorSignupForm()

    return render(request, 'users/signup_tutor.html', {'form': form})

#Signup Selection
@transaction.atomic
def signup_selection(request):
    return render(request, 'users/signup_selection.html')


# Profile Update View
@login_required
@transaction.atomic
def profile(request):
    user = request.user

    if user.is_student:
        profile = user.student_profile
        profile_form = StudentProfileForm(instance=profile)
    elif user.is_tutor:
        profile = user.tutor_profile
        profile_form = TutorProfileForm(instance=profile)

    user_form = CustomUserChangeForm(instance=user)

    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, instance=user)
        if profile_form:
            profile_form = profile_form.__class__(request.POST, request.FILES, instance=profile)  # Note the request.FILES here
        if user_form.is_valid() and (profile_form is None or profile_form.is_valid()):
            user_form.save()
            if profile_form:
                profile_form.save()
            messages.success(request, "Your profile was updated successfully.")
            return redirect('users:profile')
        else:
            messages.error(request, "Please correct the errors below.")

    return render(request, 'users/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })



# Dashboard View
@login_required
@transaction.atomic
def dashboard(request):
    if request.user.is_tutor:
        return redirect('users:tutor_dashboard')
    elif request.user.is_student:
        return redirect('users:student_dashboard')
    else:
        return redirect('home')


# Tutor Dashboard
@login_required
def tutor_dashboard(request):
    user = request.user
    profile_form = TutorProfileForm(instance=user.tutor_profile) if user.is_tutor else None
    user_form = CustomUserChangeForm(instance=user)

    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, instance=user)
        profile_form = TutorProfileForm(request.POST, request.FILES, instance=user.tutor_profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile was updated successfully.")
            return redirect('users:tutor_dashboard')
        else:
            messages.error(request, "Please correct the errors below.")

    # Check for the section in query params to determine what to display
    section = request.GET.get('section', 'overview')  # Default to overview section
    
    return render(request, 'users/tutor_dashboard.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'section': section
    })


# Student Dashboard
@login_required
def student_dashboard(request):
    user = request.user
    profile_form = StudentProfileForm(instance=user.student_profile) if user.is_student else None
    user_form = CustomUserChangeForm(instance=user)

    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, instance=user)
        profile_form = StudentProfileForm(request.POST, request.FILES, instance=user.student_profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile was updated successfully.")
            return redirect('users:student_dashboard')
        else:
            messages.error(request, "Please correct the errors below.")

    return render(request, 'users/student_dashboard.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })
