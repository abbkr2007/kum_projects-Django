# Generated by Django 3.1.2 on 2020-10-22 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pis', '0030_auto_20201023_0051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_attendence',
            name='attend',
        ),
    ]
