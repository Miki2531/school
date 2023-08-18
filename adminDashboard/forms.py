from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser  # Import your CustomUser model if it exists
from students.models import Student, Family
from classes.models import Attendance


class CustomUserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'user_role', ]

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class FamilyForm(forms.ModelForm):
    class Meta:
        model = Family
        fields = '__all__'


   
