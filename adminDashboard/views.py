from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from accounts.decorators import admin_required
from accounts.models import CustomUser
from students.models import Student
from teachers.models import Teacher
from classes.models import Class_room, Subject
from .forms import CustomUserRegistrationForm, StudentForm, FamilyForm
from employees.forms import EmployeesForm
from employees.models import Employees

from .managers import CustomUserManager

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
            form.save()
            return redirect('admin_dash:admin_dash')
    else:
        form = CustomUserRegistrationForm()

    context = {'form': form}
    return render(request, 'adminDashboard/register.html', context)

@admin_required
def create_student(request):
    if request.method == 'POST':
        student_form = StudentForm(request.POST)
        family_form = FamilyForm(request.POST)

        if student_form.is_valid() and family_form.is_valid():
            family = family_form.save()
            student = student_form.save(commit=False)

            student.family_id = family
            student.save()
            user_role_value = 'student'
            initial_data = {
                'username': student.first_name,
                'email': student.email,
                'user_role': user_role_value,
            }
            user_model = get_user_model()
            user = user_model.objects.create_user(**initial_data)
            user.set_password(student.first_name)
            user.save()
            return redirect('admin_dash:admin_dash')

    else:
        student_form = StudentForm()
        family_form = FamilyForm()

    return render(request, 'adminDashboard/create_student.html', {'student_form': student_form, 'family_form': family_form})

def create_employee(request):
    if request.method == 'POST':
        employees_form = EmployeesForm(request.POST)

        if employees_form.is_valid():
            employee = employees_form.save()
            employee.save()
            return redirect('admin_dash:admin_dash')

    else:
        employees_form = EmployeesForm()

    return render(request, 'adminDashboard/create_employee.html', {'employees_form': employees_form})


