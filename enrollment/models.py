from django.db import models
from django.contrib.auth.models import User

class Class(models.Model):
    class_name = models.CharField(max_length=100)
    class_code = models.CharField(max_length=10, unique=True)
    class_semester = models.CharField(max_length=20)
    class_year = models.PositiveIntegerField()
    class_max_enroll = models.PositiveIntegerField()
    enrolled_students = models.ManyToManyField(User, related_name='enrolled_classes', blank=True)
    class_status = models.CharField(
        max_length=10,
        choices=[('open', 'Open'), ('close', 'Close')],
        default='open'
    )

    def __str__(self):
        return self.class_name

class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    enrolled_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.student.username} - {self.enrolled_class.class_name}"
