from django.forms import ModelForm
from django import forms
from .models import Class_room, Subject, Class_subject, Attendance


""" Class room from"""
class ClassForm(ModelForm):
    """ create form for classRoom """
    class Meta:
        model= Class_room
        fields = [
            'roomName'
        ]

        widgets = {
            'roomName': forms.ChoiceField()
        }

class subjectFrom(ModelForm):
    class Meta:
        model= Subject
        fields = [
            'subjectName'
        ]

        widgets = {
            'subjectName': forms.ChoiceField()
        }

class classSubjectForm(ModelForm):
    class Meta:
        model = Class_subject
        fields = [
            'classRoomId', 'subjectId'
        ]

class attendanceForm(ModelForm):
   date = forms.DateField()

class AskDateForm(ModelForm):
    date = forms.DateField()