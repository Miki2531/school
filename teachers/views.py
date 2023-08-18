from django.shortcuts import render, redirect
from accounts.decorators import teacher_required
from accounts.models import CustomUser
from students.models import Student
from teachers.models import Teacher, Teacher_subject, ReferenceBook, Grade
from classes.models import Class_room, Subject, Attendance
from .forms import GradeUpdateForm, RefrenceBookForm

import os
from django.conf import settings
# Create your views here.
@teacher_required
def teacher_dashboard(request):
    teacher = request.user  # Assuming the logged-in user is a student
    context = {
        'teacher': teacher,
    }
    return render(request, 'teachers/teacher_dashboard.html', context)

@teacher_required
def post_student_grade(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        subject_id = request.POST.get('subject_id')
        grade_value = request.POST.get('grade')

        student = Student.objects.get(id=student_id)
        subject = Subject.objects.get(id=subject_id)

        grade, created = Grade.objects.get_or_created(student=student, subject=subject)
        grade.grade = grade_value

        return redirect('teacher_dashboard')
    students = Student.objects.all()
    subjects = Subject.objects.all()

    context = {
        'students': students,
        'subjects': subjects
    }

    return render(request, 'teachers/post_grade.html', context)


@teacher_required
def update_grade(request, grade_id):
    grade = Grade.objects.get(id=grade_id)

    if request.method == 'POST':
        new_grade_value = request.POST.get('grade')
        grade.grade = new_grade_value
        grade.save()

        return redirect('teacher_dashboard')
    context = {'grade':grade}
    return render(request, 'teachers/update_grade.html', context)

@teacher_required
def post_reference_book(request):
    if request.method == 'POST':
        book_form = RefrenceBookForm(request.POST, request.FILES)

        if book_form.is_valid():
            title = book_form.cleaned_data['title']
            file = book_form.cleaned_data['file']
        
            if file:
                file_extension = os.path.splitext(file.name)[1]
                new_file_name = f"{title}{file_extension}"

                """Construct the file path where the file to upload"""
                file_path = os.path.join(settings.MEDIA_ROOT, 'refrence_books', new_file_name)
                    
                """Save the file to specified path"""
                with open(file_path, 'wb') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)
                    
                reference_book = ReferenceBook.objects.create(title=title, file=new_file_name)
                
                return redirect('teacher_dashboard')
    book_form = RefrenceBookForm()
    teachers = Teacher.objects.all()
    context = {
        'book_form': book_form,
        'teachers': teachers,
    }

    return redirect(request, 'teachers/post_reference_book.html', context)


@teacher_required  
def mark_attendance(request):
    if request.method == 'POST':
        class_room_id = request.POST.get('class_room_id')
        section = request.POST.get('section')
        date = request.POST.get('date')
        present_status_list = request.POST.get('present_status')

        class_room = Class_room.objects.get(id=class_room_id)

        for student_id, present_status in zip(request.POST.getlist('student_id'), present_status_list):
            student = Student.objects.get(id=student_id)
            attendance = Attendance(classRoomId=class_room, section=section, date=date, present_status=present_status )
            attendance.save()

            return redirect('teacher_dashboard')
    class_room = Class_room.objects.all()
    students = Student.objects.all()
    context = {
        'class_room': class_room,
        'students': students
    }
    return render(request, 'teachers/mark_attendance.html', context)

@teacher_required
def teacher_sections(request):
    """ Display the teacher sections assigned to the teachers."""
    teacher = Teacher.objects.get(employees_id = request.user)
    teacher_sections = Teacher_subject.objects.filter(teacherId=teacher)
     
    context = {'teacher_sections', teacher_sections}
    return render(request, 'teachers/teacher_sections.html', context)