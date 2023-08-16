from django.db import models
from classes.models import Class_room

# Create your models here.
<<<<<<< HEAD
sex_choice = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

class Family_type(models.Model):
=======
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
>>>>>>> 1eeb01eeee01b72d8f3b5c559154d3ba8f51db2e
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
<<<<<<< HEAD
        return self.typeName
class Family(models.Model):
    firstName     = models.CharField(max_length=50, null=False, blank=False)
    middelName    = models.CharField(max_length=50, null=False, blank=False)
    lastName      = models.CharField(max_length=50, null=False, blank=False)
    email         = models.EmailField(max_length=100, null=False, blank=False)
    phone         = models.IntegerField(null=False, blank=False)
    sex           = models.CharField(max_length=1, null=False, blank=False, choices=sex_choice)
    family_type_id= models.ForeignKey(Family_type, on_delete= models.SET_NULL,null=True)
    def __str__(self):
        return self.firstName
class Student(models.Model):
    firstName  = models.CharField(max_length= 50, null = False, blank= False)
    middelName = models.CharField(max_length= 50, null = False, blank= False)
    lastName   = models.CharField(max_length= 50, null = False, blank= False)
    email      = models.EmailField(max_length= 100, null = False, blank= False)
    phone      = models.IntegerField(null=False, blank=False)
    age        = models.IntegerField(null = False, blank= False)
    sex        = models.CharField(max_length=1, null = False, blank= False, choices=sex_choice)
    class_room_id = models.ForeignKey(Class_room, on_delete=models.SET_NULL, null=True)
    family_id = models.ForeignKey(Family, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.firstName
=======
        return self.first_name
>>>>>>> 1eeb01eeee01b72d8f3b5c559154d3ba8f51db2e
    



