from django.contrib import admin
from .models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    # List the fields to be displayed in the admin panel
    list_display = ('doctor', 'patient', 'appointment_date', 'appointment_time')
    
    # Allow filtering by doctor and appointment date
    list_filter = ('doctor', 'appointment_date')

    # Make fields clickable in the list view
    search_fields = ('doctor__first_name', 'doctor__last_name', 'patient__first_name', 'patient__last_name')

    # Optionally, add ordering based on date and time of appointment
    ordering = ('appointment_date', 'appointment_time')

    # Make the fields readonly for some information in the admin detail view
    readonly_fields = ('doctor', 'patient', 'appointment_date', 'appointment_time')

# Register the Appointment model along with its custom admin class
admin.site.register(Appointment, AppointmentAdmin)
