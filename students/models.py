from django.db import models
from classes.models import Class_room

# Create your models here.
class Family(models.Model):
    first_name_f     = models.CharField(max_length=50, null=False, blank=False)
    last_name_f    = models.CharField(max_length=50, null=False, blank=False)
    email_f         = models.EmailField(max_length=100, null=False, blank=False)
    phone_f = models.CharField(max_length=15, blank=False, null=False)
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    gender_f = models.CharField(max_length=1, choices=gender_choices)
    address_f = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.first_name_f
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    gender = models.CharField(max_length=1, choices=gender_choices)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    register_date = models.DateField(auto_now_add=True)
    class_room_id = models.ForeignKey(Class_room, on_delete=models.SET_NULL, null=True)
    Family_type_choice = (
        ('Mother', 'Mother'),
        ('Father', 'Father'),
        ('Auncle', 'Auncle'),
        ('Aunt', 'Aunt'),
        ('GrandMa', 'GrandMa'),
        ('GrandPa', 'GrandPa')
    )
    typeName = models.CharField(max_length=50, null=False, blank=False, choices=Family_type_choice)
    family_id = models.ForeignKey(Family, on_delete=models.SET_NULL, blank= True
                                  , null=True)
    def __str__(self):
        return self.first_name
    



