# Generated by Django 3.1.2 on 2020-10-19 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0035_semester_advisor'),
    ]

    operations = [
        migrations.AddField(
            model_name='semester',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='semester_course', to='sis.course'),
        ),
    ]