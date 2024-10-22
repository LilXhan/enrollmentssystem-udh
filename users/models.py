from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12, null=True)
    dni = models.CharField(max_length=8)
    birth_date = models.DateField(null=True)
    address = models.CharField(max_length=50, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dni = models.CharField(max_length=8, unique=True)
    birth_date = models.DateField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


def certificate_upload_path(instance, filename):
    return f'certificates/{instance.student.dni}.pdf'

class StudyCertificate(models.Model):
    verification_status_choices = (
        ('VERIFIED', 'Verified'),
        ('PENDING', 'Pending'),
        ('REJECTED', 'Rejected')
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE) 
    certified_file = models.FileField(upload_to=certificate_upload_path, null=True, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    verification_status = models.CharField(choices=verification_status_choices, default='PENDING', max_length=10)