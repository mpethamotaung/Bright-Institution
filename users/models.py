from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

# Abstract base profile model to avoid redundancy
class Profile(models.Model):
    bio = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.png', blank=True)

    class Meta:
        abstract = True

class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_tutor = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class TutorProfile(Profile):
    class SubjectChoices(models.TextChoices):
        MATHEMATICS = 'Mathematics', 'Mathematics'
        SCIENCE = 'Science', 'Science'
        BOTH = 'Both', 'Both'

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tutor_profile')
    subjects = models.CharField(max_length=255, choices=SubjectChoices.choices, null=True, blank=True)
    availability = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class StudentProfile(Profile):
    class GradeChoices(models.TextChoices):
        GRADE_7 = 'Grade 7', 'Grade 7'
        GRADE_8 = 'Grade 8', 'Grade 8'
        GRADE_9 = 'Grade 9', 'Grade 9'
        GRADE_10 = 'Grade 10', 'Grade 10'
        GRADE_11 = 'Grade 11', 'Grade 11'
        GRADE_12 = 'Grade 12', 'Grade 12'


    class SubjectChoices(models.TextChoices):
        MATHEMATICS = 'Mathematics', 'Mathematics'
        SCIENCE = 'Science', 'Science'
        BOTH = 'Both', 'Both'

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student_profile')
    grade = models.CharField(max_length=20, choices=GradeChoices.choices, null=True, blank=True)
    subjects = models.CharField(max_length=50, choices=SubjectChoices.choices, default=SubjectChoices.BOTH)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=CustomUser)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_student:
            StudentProfile.objects.get_or_create(user=instance)
        elif instance.is_tutor:
            TutorProfile.objects.get_or_create(user=instance)
    else:
        # Update the profile in case it was modified directly
        if instance.is_student and hasattr(instance, 'student_profile'):
            instance.student_profile.save()
        if instance.is_tutor and hasattr(instance, 'tutor_profile'):
            instance.tutor_profile.save()
