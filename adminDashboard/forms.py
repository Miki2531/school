from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
<<<<<<< HEAD
from accounts.models import CustomUser
from students.models import Family, Family_type, Student  # Import your CustomUser model if it exists

class CustomUserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser  # Use your CustomUser model here
        fields = ['username', 'email', 'user_role']  # Add other fields as needed


class FamilyTypeSelector(ModelForm):
    class Meta:
        model = Family_type
        fields = [
            'typeName'
        ]
        widgets = {
            'typeName': forms.Select()
        }

class FamilyForm(ModelForm):
    class Meta:
        model = Family
        fields = [
            'firstName', 'middelName', 'lastName', 'email', 'phone', 'sex', 'family_type_id'
        ]

        widgets = {
            'sex': forms.Select()
        }
class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = [
            'firstName', 'middelName', 'lastName', 'email', 'phone', 'sex', 'class_room_id', 'family_type_id'
        ]

        widgets = {
            'sex': forms.Select()
        }
=======
from accounts.models import CustomUser  # Import your CustomUser model if it exists
from students.models import Student, Family

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
>>>>>>> 1eeb01eeee01b72d8f3b5c559154d3ba8f51db2e
