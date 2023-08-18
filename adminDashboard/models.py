from django.db import models
from classes.models import Class_student
# Create your models here.

class School_Year(models.Model):
    year_name = models.CharField(max_length=9, unique=True, help_text="Format: YYYY-YYYY (e.g., 2023-2024)")

    def __str__(self):
        return self.year_name

    class Meta:
        verbose_name_plural = "School Years"
class School_Year_Class(models.Model):
    schoolYear = models.ForeignKey(School_Year, on_delete=models.SET_NULL, null=True, blank=False)
    student_in_class = models.ForeignKey(Class_student, on_delete=models.SET_NULL, null=True, blank=False)
    free = models.IntegerField()



