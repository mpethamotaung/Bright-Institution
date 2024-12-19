from django.db import models
from users.models import TutorProfile, StudentProfile

class Booking(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='bookings')
    tutor = models.ForeignKey(TutorProfile, on_delete=models.CASCADE, related_name='bookings')
    date = models.DateField()
    time = models.TimeField()
    subject = models.CharField(max_length=100, default='Default Subject')
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Booking: {self.student.user.username} with {self.tutor.user.username} on {self.date} at {self.time}"
