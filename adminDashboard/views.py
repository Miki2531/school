from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from accounts.decorators import admin_required
from students.models import Student
from teachers.models import Teacher
from classes.models import Class_room, Subject
from .forms import CustomUserRegistrationForm, StudentForm, FamilyForm

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

@admin_required
def create_student(request):
    if request.method == 'POST':
        student_form = StudentForm(request.POST)
        family_form = FamilyForm(request.POST)

        if student_form.is_valid() and family_form.is_valid():
            print(StudentForm(request.POST).data)
            family = family_form.save()
            student = student_form.save(commit=False)

            student.family_id = family
            student.save()
            return redirect('admin_dash:admin_dash')
    else:
        student_form = StudentForm()
        family_form = FamilyForm()

    return render(request, 'adminDashboard/create_student.html', {'student_form': student_form, 'family_form': family_form})
