# Generated by Django 4.2.7 on 2023-12-05 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeApp', '0004_chkboxcourse'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='coursename',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
