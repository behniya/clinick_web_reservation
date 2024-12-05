from django.urls import path
from .views import doctor_signup , patient_signup , login_view , logout_view

urlpatterns = [
    path('signup/doctors/' , doctor_signup , name = 'doctor_signup'),
    path('signup/patient/' , patient_signup , name = 'patient_signup'),
    path('login/' , login_view , name='login'),
    path('logout/' , logout_view , name='logout'),
]