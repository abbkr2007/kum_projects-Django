# Generated by Django 3.1.2 on 2020-11-06 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0053_auto_20201106_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='semester_1st',
            name='dept',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='department_1st_semester', to='sis.department'),
        ),
        migrations.AddField(
            model_name='semester_1st',
            name='program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='program_1st_semester', to='sis.program'),
        ),
        migrations.AddField(
            model_name='semester_2nd',
            name='dept',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='department_2nd_semester', to='sis.department'),
        ),
        migrations.AddField(
            model_name='semester_2nd',
            name='program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='program_2nd_semester', to='sis.program'),
        ),
        migrations.AddField(
            model_name='semester_3rd',
            name='dept',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='department_3rd_semester', to='sis.department'),
        ),
        migrations.AddField(
            model_name='semester_3rd',
            name='program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='program_3rd_semester', to='sis.program'),
        ),
        migrations.AddField(
            model_name='semester_4th',
            name='dept',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='department_4th_semester', to='sis.department'),
        ),
        migrations.AddField(
            model_name='semester_4th',
            name='program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='program_4th_semester', to='sis.program'),
        ),
        migrations.AddField(
            model_name='semester_5th',
            name='dept',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='department_5th_semester', to='sis.department'),
        ),
        migrations.AddField(
            model_name='semester_5th',
            name='program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='program_5th_semester', to='sis.program'),
        ),
        migrations.AddField(
            model_name='semester_6th',
            name='dept',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='department_6th_semester', to='sis.department'),
        ),
        migrations.AddField(
            model_name='semester_6th',
            name='program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='program_6th_semester', to='sis.program'),
        ),
    ]