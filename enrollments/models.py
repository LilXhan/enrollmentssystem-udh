from django.db import models
from users.models import User

class Enrollment(models.Model):
    enrollment_status_choices = (
        ('ACTIVATE', 'Activate'),
        ('PENDING', 'Pending'),
        ('CANCELED', 'Canceled')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
    enrollment_status = models.CharField(choices=enrollment_status_choices, default='PENDING', max_length=10)


class Payment(models.Model):
    payment_status_choices = (
        ('VERIFIED', 'Verified'),
        ('PENDING', 'Pending'),
        ('CANCELED', 'Canceled')
    )

    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    payment_date = models.DateField()
    amount = models.FloatField(default=459.99)
    payment_status = models.CharField(payment_status_choices, default='PENDING', max_length=10)
    payment_method = models.CharField(max_length=50)
