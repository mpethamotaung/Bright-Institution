from django import forms
from .models import Booking
from users.models import TutorProfile

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['tutor', 'date', 'time', 'subject', 'notes']

    def __init__(self, *args, **kwargs):
        student = kwargs.pop('student', None)
        super(BookingForm, self).__init__(*args, **kwargs)
        if student:
            self.fields['tutor'].queryset = TutorProfile.objects.filter(subjects__icontains=student.subjects)
