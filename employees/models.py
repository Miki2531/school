from django.db import models
class Employees(models.Model):
    firstName = models.CharField(max_length=50, null=False, blank=False)
    lastName = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    phone = models.IntegerField(null=False, blank=False)
    address = models.CharField(max_length=50, null=False, blank=False)
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    gender = models.CharField(max_length=10, choices=gender_choices)
    registrationDate = models.DateField(auto_now_add= True)
    Job_Type = (
        ('Director', 'Director'),
        ('Vice Director', 'Vice Director'),
        ('Secretery', 'Secretery'),
        ('Accountant', 'Accountant'),
        ('Teacher', 'Teacher'),
        ('Janitor', 'Janitor'),
        ('Security Gard', 'Security Gard'),
        ('Gardener', 'Gardener'),

    )
    title = models.CharField(max_length=50, null=False, blank=False, choices=Job_Type)
    def __str__(self):
        return self.title
