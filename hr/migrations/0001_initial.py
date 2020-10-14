# Generated by Django 3.1.2 on 2020-10-11 06:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pis', '0002_auto_20201009_1822'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sis', '0006_department_tution'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hr_Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=10)),
                ('pin_number', models.CharField(max_length=100, unique=True)),
                ('first_name', models.CharField(max_length=40)),
                ('middle_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('image', models.ImageField(upload_to='lecturer/images/')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('marital_status', models.CharField(choices=[('single', 'Single'), ('married', 'Married')], max_length=10)),
                ('child', models.PositiveIntegerField()),
                ('date_of_birth', models.DateField(default=django.utils.timezone.now)),
                ('graduate', models.IntegerField()),
                ('postgraduate', models.IntegerField()),
                ('phd', models.IntegerField()),
                ('date_of_join', models.DateField(default=django.utils.timezone.now)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.TextField(blank=True)),
                ('others', models.TextField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Hr_Manager',
                'verbose_name_plural': 'Hr_Managers',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Control_Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(upload_to='sis/files/')),
                ('notice', models.TextField()),
                ('text', models.CharField(max_length=150)),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sis.student')),
            ],
            options={
                'verbose_name': 'Control_Student',
                'verbose_name_plural': 'Control_Students',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Control_Lecturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(upload_to='hr/files/')),
                ('notice', models.TextField()),
                ('text', models.CharField(max_length=150)),
                ('lecturer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pis.lecturer')),
            ],
            options={
                'verbose_name': 'Control_Lecturer',
                'verbose_name_plural': 'Control_Lecturers',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
