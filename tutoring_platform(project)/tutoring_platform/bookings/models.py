from django.db import models
from users.models import CustomUser

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Booking(models.Model):
    student = models.ForeignKey(CustomUser, related_name='student_bookings', on_delete=models.CASCADE)
    tutor = models.ForeignKey(CustomUser, related_name='tutor_bookings', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateTimeField()
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.username} - {self.tutor.username} on {self.date}"
