from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from accounts.decorators import admin_required
from students.models import Student
from teachers.models import Teacher
from classes.models import Class_room, Subject
from .forms import CustomUserRegistrationForm
from .forms import FamilyTypeSelector, FamilyForm, StudentForm

@admin_required
def admin_dash(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    classes = Class_room.objects.all()
    subjects = Subject.objects.all()

    context = {
        'students': students,
        'teachers': teachers,
        'classes': classes,
        'subjects': subjects,
    }

    return render(request, 'adminDashboard/test.html', context)
@admin_required
def register_user(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user
            return redirect('admin_dash:admin_dash')
    else:
        form = CustomUserRegistrationForm()

    context = {'form': form}
    return render(request, 'adminDashboard/register.html', context)




def family_type_selector_view(request):
    if request.method == 'POST':
        form = FamilyTypeSelector(request.POST)
        if form.is_valid():
            selected_type = form.cleaned_data['typeName']
            if selected_type == 'Parent':
                return redirect('family_registration')
            elif selected_type == 'Guardian':
                return redirect('student_registration')
            else:
                return redirect('invalid_selection')
    else:
        form = FamilyTypeSelector()
    
    return render(request, 'family_type_selector.html', {'form': form})

def family_registration_view(request):
    if request.method == 'POST':
        form = FamilyForm(request.POST)
        if form.is_valid():
            family = form.save()  
            return redirect('family_registration_success')
    else:
        form = FamilyForm()
    
    return render(request, 'adminDashboard\family_registration.html', {'form': form})

def student_registration_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()  
            return redirect('student_registration_success')
    else:
        form = StudentForm()
    
    return render(request, 'adminDashboard\student_registration.html', {'form': form})
