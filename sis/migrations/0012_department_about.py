# Generated by Django 3.1.2 on 2020-10-12 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0011_department_enrolled'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='about',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
