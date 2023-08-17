from django.db import models

# Create your models here.

class SchoolYear(models.Model):
    year_name = models.CharField(max_length=9, unique=True, help_text="Format: YYYY-YYYY (e.g., 2023-2024)")

    def __str__(self):
        return self.year_name

    class Meta:
        verbose_name_plural = "School Years"