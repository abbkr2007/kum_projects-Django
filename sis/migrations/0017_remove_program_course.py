# Generated by Django 3.1.2 on 2020-10-13 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0016_auto_20201013_1211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='course',
        ),
    ]
