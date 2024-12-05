from django.shortcuts import render, redirect
from django.contrib.auth import login , logout
from .forms import DoctorSignUpForms, PatientSignUpForms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login
from django.contrib import messages

def doctor_signup(request):
    if request.method == 'POST':
        form = DoctorSignUpForms(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to doctor's dashboard
    else:
        form = DoctorSignUpForms()
    return render(request, 'registrations/doctor_signup.html', {'form': form})

def patient_signup(request):
    if request.method == 'POST':
        form = PatientSignUpForms(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to patient's dashboard
    else:
        form = PatientSignUpForms()
    return render(request, 'registrations/patient_signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request , data = request.POST)
        if form.is_valid():
            # Authenticate the user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request , username=username , password=password)

            if user is not None:
                login(request , user)
                # Check if the user is a doctor or patient and redirect accordingly
                if user.is_doctor:
                    return redirect('home')
                elif user.is_patient:
                    return redirect('home')
                else:
                    return redirect('home')
            else:
                messages.error('Invalid username or password')
                return redirect('login')
    else:
        form = AuthenticationForm()

    return render(request, 'registrations/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')