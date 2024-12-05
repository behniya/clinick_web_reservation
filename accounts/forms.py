from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class DoctorSignUpForms(UserCreationForm):
    SKILL_CHOICES = [
        ('cardiology', 'Cardiology'),
        ('pediatrics', 'Pediatrics'),
        ('neurology', 'Neurology'),
        ('orthopedics', 'Orthopedics'),
        ('dermatology', 'Dermatology'),
    ]
    
    skills = forms.ChoiceField(
        choices=SKILL_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Specialization/Skills",
        required=True
    )
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name' , 'last_name' , 'skills', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.is_doctor = True                      # Mark the user as a doctor
        user.skills = self.cleaned_data['skills']  # Save the selected skill
        if commit:
            user.save()
        return user


class PatientSignUpForms(UserCreationForm):
    phone_number = forms.CharField(
        max_length=13,  # "+98XXXXXXXXXX"
        widget=forms.TextInput(attrs={'placeholder': '+98XXXXXXXXXX', 'value': '+98'}),
        required=True,
        label="Phone Number"
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number.startswith('0'):  # Replace leading '0' with '+98'
            phone_number = '+98' + phone_number[1:]
        if not phone_number.startswith('+98') or len(phone_number) != 13:
            raise forms.ValidationError('Phone number must be in the format +98XXXXXXXXXX.')
        return phone_number

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_patient = True  # Mark the user as a patient
        user.phone_number = self.cleaned_data['phone_number']  # Save phone number
        if commit:
            user.save()
        return user
