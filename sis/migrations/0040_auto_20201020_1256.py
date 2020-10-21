# Generated by Django 3.1.2 on 2020-10-20 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0039_auto_20201019_2224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semester',
            name='course',
        ),
        migrations.AddField(
            model_name='semester',
            name='course',
            field=models.ManyToManyField(blank=True, related_name='semester_course', to='sis.Course'),
        ),
    ]
