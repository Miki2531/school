from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser
from students.models import Family, Family_type, Student  # Import your CustomUser model if it exists

class CustomUserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser  # Use your CustomUser model here
        fields = ['username', 'email', 'user_role']  # Add other fields as needed

class FamilyForm(ModelForm):
    class Meta:
        model = Family
        fields = [
            'firstName', 'middelName', 'lastName', 'email', 'phone', 'sex', 'family_type_id'
        ]

        widgets = {
            'sex': forms.ChoiceField()
        }
class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = [
            'firstName', 'middelName', 'lastName', 'email', 'phone', 'sex', 'class_room_id', 'family_type_id'
        ]

        widgets = {
            'sex': forms.ChoiceField()
        }