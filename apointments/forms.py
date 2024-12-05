from django import forms
from django.core.exceptions import ValidationError
from .models import Appointment
from datetime import datetime

class DoctorSearchForm(forms.Form):
    query = forms.CharField(max_length=100 , required=False , label='Search for a doctor or skill')

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['appointment_date' , 'appointment_time']

    appointment_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'min': datetime.today().date()}),  # Set minimum date to today
        required=True
    )

    def __init__(self, *args, **kwargs):
        self.doctor = kwargs.pop('doctor', None)
        super(AppointmentForm, self).__init__(*args, **kwargs)

    def clean_appointment_date(self):
        appointment_date = self.cleaned_data.get('appointment_date')
        if appointment_date < datetime.today().date():
            raise ValidationError("The appointment date cannot be in the past.")
        return appointment_date
    
    time_choice = [
        ('8:00' , '8:00'),
        ('8:30' , '8:30'),
        ('9:00' , '9:00'),
        ('9:30' , '9:30'),
        ('10:00' , '10:00'),
        ('10:30' , '10:30'),
        ('11:00' , '11:00'),
        ('11:30' , '11:30'),
        ('12:00' , '12:00'),
        ('12:30' , '12:30'),
        ('13:00' , '13:00'),
        ('13:30' , '13:30'),
        ('14:00' , '14:30'),
        ('15:00' , '15:00'),
        ('15:30' , '15:30'),
        ('16:00' , '16:30'),
        ('17:00' , '17:00'),
        ('17:30' , '17:30'),
        ('18:00' , '18:00'),
    ]

    appointment_time = forms.ChoiceField(choices=time_choice , required=True)

    def clean_appointment_time(self):
        appointment_date = self.cleaned_data.get('appointment_date')
        appointment_time = self.cleaned_data.get('appointment_time')

        existing_appointment = Appointment.objects.filter(
            doctor = self.doctor,
            appointment_date = appointment_date,
            appointment_time = appointment_time
        )

        if existing_appointment.exists():
            raise ValidationError(f"The time slot {appointment_time} on {appointment_date} is already taken by another user. Please select a different time.")
        return appointment_time