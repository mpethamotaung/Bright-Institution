from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from .models import CustomUser, StudentProfile, TutorProfile

# Student Signup Form
class StudentSignupForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Email Address'})
    )
    grade = forms.ChoiceField(
        choices=StudentProfile.GradeChoices.choices,
        required=True,
        widget=forms.Select(attrs={'placeholder': 'Grade'})
    )
    subjects = forms.MultipleChoiceField(
        choices=StudentProfile.SubjectChoices.choices,
        required=True,
        widget=forms.CheckboxSelectMultiple()
    )

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', 'grade', 'subjects')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("A user with this email already exists.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_student = True
        user.is_tutor = False
        user.username = user.email
        if commit:
            user.save()
            # Create student profile
            StudentProfile.objects.create(
                user=user,
                grade=self.cleaned_data['grade'],
                subjects=self.cleaned_data['subjects']
            )
        return user


# Tutor Signup Form
class TutorSignupForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Email Address'})
    )
    subjects = forms.MultipleChoiceField(
        choices=TutorProfile.SubjectChoices.choices,
        required=True,
        widget=forms.CheckboxSelectMultiple()
    )
    availability = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Availability'})
    )

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', 'subjects', 'availability')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("A user with this email already exists.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_student = False
        user.is_tutor = True
        user.username = user.email
        if commit:
            user.save()
            # Create tutor profile
            TutorProfile.objects.create(
                user=user,
                subjects=self.cleaned_data['subjects'],
                availability=self.cleaned_data['availability']
            )
        return user


# Custom User Change Form
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'is_student', 'is_tutor')


# Student Profile Form (used to edit student profile)
class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['bio', 'phone', 'email', 'profile_picture', 'grade', 'subjects']


# Tutor Profile Form (used to edit tutor profile)
class TutorProfileForm(forms.ModelForm):
    class Meta:
        model = TutorProfile
        fields = ['bio', 'phone', 'email', 'profile_picture', 'subjects', 'availability']
