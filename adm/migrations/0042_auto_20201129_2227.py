# Generated by Django 3.1.2 on 2020-11-29 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0041_auto_20201129_1918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admission',
            name='dept',
        ),
        migrations.RemoveField(
            model_name='admission',
            name='faculty',
        ),
        migrations.RemoveField(
            model_name='admission',
            name='registration_No',
        ),
    ]