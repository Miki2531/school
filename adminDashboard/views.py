from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from accounts.decorators import admin_required
from students.models import Student
from teachers.models import Teacher
from classes.models import Class_room, Subject

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