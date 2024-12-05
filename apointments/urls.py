from django.urls import path
from .views import home , search_doctors , book_appointment , appointment_success

urlpatterns = [
    path('' , home , name='home'),
    path('search/' , search_doctors , name='search_doctors'),
    path('book_appointment/<int:doctor_id>/' , book_appointment , name='book_appointment'),
    path('appointment_success/', appointment_success, name='appointment_success'),
]