# Generated by Django 3.1.2 on 2020-10-22 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pis', '0023_auto_20201022_1019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance_report',
            old_name='subject',
            new_name='student',
        ),
    ]
