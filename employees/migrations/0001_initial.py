# Generated by Django 4.0.7 on 2023-08-16 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('registrationDate', models.DateField(auto_now_add=True)),
                ('title', models.CharField(choices=[('Director', 'Director'), ('Vice Director', 'Vice Director'), ('Secretery', 'Secretery'), ('Accountant', 'Accountant'), ('Teacher', 'Teacher'), ('Janitor', 'Janitor'), ('Security Gard', 'Security Gard'), ('Gardener', 'Gardener')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Director', 'Director'), ('Vice Director', 'Vice Director'), ('Secretery', 'Secretery'), ('Accountant', 'Accountant'), ('Teacher', 'Teacher'), ('Janitor', 'Janitor'), ('Security Gard', 'Security Gard'), ('Gardener', 'Gardener')], max_length=50)),
            ],
        ),
    ]
