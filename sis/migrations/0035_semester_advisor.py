# Generated by Django 3.1.2 on 2020-10-19 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pis', '0010_auto_20201019_1135'),
        ('sis', '0034_semester'),
    ]

    operations = [
        migrations.AddField(
            model_name='semester',
            name='advisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='semester_advisor', to='pis.lecturer'),
        ),
    ]