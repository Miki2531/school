from django import forms
from django.forms import ModelForm
from .models import ReferenceBook, Grade, Teacher_subject, Teacher

class TeacherSubjectForm(forms.ModelForm):
    class Meta:
        model = Teacher_subject
        fields = '__all__'

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

class GradeUpdateForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'subject', 'grade']

class RefrenceBookForm(forms.ModelForm):
    class Meta:
        model = ReferenceBook
        fields = '__all__'