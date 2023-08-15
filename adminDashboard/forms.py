from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser  # Import your CustomUser model if it exists
from students.models import Student, Family

class CustomUserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser  # Use your CustomUser model here
        fields = ['username', 'email', 'user_role']  # Add other fields as needed

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class FamilyForm(forms.ModelForm):
    class Meta:
        model = Family
        fields = '__all__'
