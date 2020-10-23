# Generated by Django 3.1.2 on 2020-10-22 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pis', '0024_auto_20201022_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance_report',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subject_attendance_reprot', to='pis.subject_attendence'),
        ),
        migrations.AlterField(
            model_name='attendance_report',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_attendance_report', to='pis.student_attendence'),
        ),
    ]