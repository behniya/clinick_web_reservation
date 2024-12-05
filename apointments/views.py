from django.shortcuts import render , redirect , get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from accounts.models import CustomUser  
from .forms import DoctorSearchForm
from .forms import AppointmentForm

def home(request):
    form = DoctorSearchForm()
    doctors = None
    if 'query' in request.GET:
        query = request.GET['query']
        doctors = CustomUser.objects.filter(
            is_doctor=True,  # Filter only doctors
            first_name__icontains=query
        ) | CustomUser.objects.filter(
            is_doctor=True,  # Filter only doctors
            last_name__icontains=query
        ) | CustomUser.objects.filter(
            is_doctor=True,  # Filter only doctors
            skills__icontains=query
        )
    return render(request, 'home.html', {'form': form, 'doctors': doctors})

def search_doctors(request):
    query = request.GET.get('query', '')
    doctors = CustomUser.objects.filter(
        is_doctor=True,  # Only doctors
        first_name__icontains=query
    ) | CustomUser.objects.filter(
        is_doctor=True,  # Only doctors
        last_name__icontains=query
    ) | CustomUser.objects.filter(
        is_doctor=True,  # Only doctors
        skills__icontains=query
    )
    
    # Prepare the doctor data to be returned as JSON
    doctor_list = list(doctors.values('first_name', 'last_name', 'skills' , 'id'))
    return JsonResponse({'doctors': doctor_list})

def book_appointment(request , doctor_id):
    doctor = get_object_or_404(CustomUser , id=doctor_id , is_doctor=True)

    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = AppointmentForm(request.POST , doctor=doctor)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.doctor = doctor
            appointment.patient = request.user
            appointment.save()
            return redirect('appointment_success')  
    else:
        form = AppointmentForm(doctor=doctor)

    return render(request, 'appointments/book_appointment.html', {'form': form, 'doctor': doctor})

def appointment_success(request):
    return render(request, 'appointments/appointment_success.html')