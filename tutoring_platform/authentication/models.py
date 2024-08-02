from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('tutor', 'Tutor'),
        ('admin', 'Admin'),
    )
    user_type = models.CharField(
        max_length=10,
        choices=USER_TYPE_CHOICES,
        default='student',
    )
    # Additional fields can be added here if needed

class StudentProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='student_profile')
    # Add fields specific to students
    bio = models.TextField(blank=True, null=True)
    # Other fields such as profile picture, etc.

class TutorProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='tutor_profile')
    # Add fields specific to tutors
    qualifications = models.TextField(blank=True, null=True)
    subjects = models.ManyToManyField('Subject', blank=True)
    # Other fields such as availability, rates, etc.

class Subject(models.Model):
    name = models.CharField(max_length=100)
    # Other fields related to subjects can be added here

    def __str__(self):
        return self.name
