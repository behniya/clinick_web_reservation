from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'is_doctor', 'is_patient', 'first_name' , 'last_name' , 'phone_number' , 'skills', 'is_staff', 'is_active']  # Added skills to list_display
    list_filter = ['is_doctor', 'is_patient', 'is_staff', 'is_active']
    search_fields = ['username', 'email']
    ordering = ['username']

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email', 'skills')  # Added skills to personal info
        }),
        ('Permissions', {
            'fields': ('is_doctor', 'is_patient', 'is_active', 'is_staff', 'groups', 'user_permissions')
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_doctor', 'is_patient', 'is_active', 'skills' , 'first_name' , 'last_name' , 'phone_number')  # Added skills to add form
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
