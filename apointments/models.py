from django.db import models
from django.contrib.auth import get_user_model

class Appointment(models.Model):
    doctor = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        limit_choices_to={'is_doctor': True},
        related_name='appointments_as_doctor'  # Unique related name for doctor
    )
    patient = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        limit_choices_to={'is_patient': True},
        related_name='appointments_as_patient'  # Unique related name for patient
    )
    appointment_date = models.DateField()
    appointment_time = models.TimeField()

    class Meta:
        unique_together = ('doctor', 'appointment_date', 'appointment_time')

    def __str__(self):
        return f"Appointment with Dr. {self.doctor.first_name} {self.doctor.last_name} on {self.appointment_date} at {self.appointment_time}"
