from django.db import models
from employees.models import Employees
from classes.models import Subject
from students.models import Student
# Create your models here.

class Teacher(models.Model):
    employees_id = models.ForeignKey(Employees, on_delete= models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.employees_id.__str__()
class Teacher_subject(models.Model):
    teacherId = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=False)
    subjectId = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=False)
    def __str__(self):
        return self.teacherId.__str__() + ' ' + self.subjectId.__str__()
    
class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.CharField(max_length=10) 
    
    def __str__(self):
        return f"{self.student.student_name} - {self.subject.subjectName}: {self.grade}"
    
class ReferenceBook(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='reference_books/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    fileUploadedBy = models.ForeignKey(Teacher, on_delete= models.CASCADE, null=True)

    def __str__(self):
        return self.title