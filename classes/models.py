from django.db import models

# Create your models here.
class Class_room(models.Model):
    GreadClass_chocice = (
        ('Gread 9', 'G9'),
        ('Gread 10', 'G10'),
        ('Gread 11', 'G11'),
        ('Gread 12', 'G12')
    )
    roomName = models.CharField(max_length=50, null=False, blank=False,  choices=GreadClass_chocice)
    def __str__(self):
        return self.roomName
class Subject(models.Model):
    Subject_Choice = (
          ('Bio', 'Biology'),
          ('Chemo', 'Chemistry'),
          ('Math', 'Mathimatics'),
          ('Eng', 'English'),
          ('Pyh', 'Pyhsics'),
          ('Civ', 'Civics'),
          ('Eco', 'Economics'),
          ('It', 'Information Technology'),
          ('Dre', 'Dreawing')

    )
    subjectName = models.CharField(max_length=50, null=False, blank=False, choices=Subject_Choice)
    def __str__(self):
        return self.subjectName

class Class_subject(models.Model):
    classRoomId = models.ForeignKey(Class_room, on_delete=models.SET_NULL, null=True, blank=False)
    subjectId = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=False)
    def __str__(self):
        return self.classRoomId.__str__() + ' ' + self.subjectId.__str__()