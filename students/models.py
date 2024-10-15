from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    enrollment_number = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.name} ({self.enrollment_number})"
