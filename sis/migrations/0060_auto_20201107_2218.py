# Generated by Django 3.1.2 on 2020-11-07 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0059_auto_20201107_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='currentstatus',
            name='semester',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_courent_semester', to='sis.semester'),
        ),
        migrations.AlterField(
            model_name='currentstatus',
            name='course',
            field=models.ManyToManyField(blank=True, related_name='student_curent_courses', to='sis.Courses'),
        ),
        migrations.AlterField(
            model_name='currentstatus',
            name='dept',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_curent_department', to='sis.department'),
        ),
        migrations.AlterField(
            model_name='currentstatus',
            name='faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_curent_faculty', to='sis.faculty'),
        ),
        migrations.AlterField(
            model_name='currentstatus',
            name='program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_curent_program', to='sis.program'),
        ),
        migrations.CreateModel(
            name='Course_Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currentstatus', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_course_reg', to='sis.currentstatus')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sis.student')),
            ],
        ),
    ]