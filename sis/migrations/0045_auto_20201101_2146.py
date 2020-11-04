# Generated by Django 3.1.2 on 2020-11-01 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0044_auto_20201027_0256'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'managed': True, 'verbose_name': 'Student', 'verbose_name_plural': 'Students'},
        ),
        migrations.CreateModel(
            name='Student_Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('message_status', models.IntegerField(default=0)),
                ('sent_date', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sis.student')),
            ],
        ),
    ]
