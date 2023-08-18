# Generated by Django 4.0.7 on 2023-08-17 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class_room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomName', models.CharField(choices=[('Gread 8', 'G8'), ('Gread 9', 'G9'), ('Gread 10', 'G10'), ('Gread 11', 'G11'), ('Gread 12', 'G12')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjectName', models.CharField(choices=[('Bio', 'Biology'), ('Chemo', 'Chemistry'), ('Math', 'Mathimatics'), ('Eng', 'English'), ('Pyh', 'Pyhsics'), ('Civ', 'Civics'), ('Eco', 'Economics'), ('It', 'Information Technology'), ('Dre', 'Dreawing')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Class_subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classRoomId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='classes.class_room')),
                ('subjectId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='classes.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Class_student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classRoomId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='classes.class_room')),
                ('studentID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='students.student')),
            ],
        ),
    ]
