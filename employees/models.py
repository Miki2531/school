from django.db import models

# Create your models here.
class Job(models.Model):
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
class Employees(models.Model):
    firstName = models.CharField(max_length=50, null=False, blank=False)
    middelName = models.CharField(max_length=50, null=False, blank=False)
    lastName = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    phone = models.IntegerField(null=False, blank=False)
    address = models.CharField(max_length=50, null=False, blank=False)
    sex = models.CharField(max_length=1, null=False, blank=False)
    registrationDate = models.DateField(auto_now_add= True)
    Job_id = models.ForeignKey(Job, on_delete= models.SET_NULL, null=True)

    def __str__(self):
        return self.firstName
