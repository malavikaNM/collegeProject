# Generated by Django 4.2.7 on 2023-12-06 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeApp', '0007_remove_students_coursename_students_coursename'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='materials_provide',
        ),
        migrations.AlterField(
            model_name='students',
            name='coursename',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
