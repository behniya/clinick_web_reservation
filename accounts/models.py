from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100 , blank=False , null=False)
    last_name = models.CharField(max_length=100 , blank=False , null=False)
    phone_number = models.CharField(
                max_length=13, # "+98" (3) + 10 digits (10)
        validators=[
            RegexValidator(
                regex = r'^\+98\d{10}$',
                message = 'Phone number must start with +98 and have 10 digits after it')
        ],
        blank=True,
        null=True
    )

    skills = models.CharField(max_length=255 , blank=True , null=True)
