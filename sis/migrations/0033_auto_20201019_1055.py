# Generated by Django 3.1.2 on 2020-10-19 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pis', '0008_auto_20201019_1055'),
        ('sis', '0032_auto_20201019_0807'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester_Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('session_start', models.DateField()),
                ('session_end', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='SessionYearModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_start_year', models.DateField()),
                ('session_end_year', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Semester',
        ),
    ]
