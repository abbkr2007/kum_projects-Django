# Generated by Django 3.1.2 on 2020-10-09 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0003_auto_20201009_1701'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subject',
            options={'managed': True, 'verbose_name': 'Subject', 'verbose_name_plural': 'Subjects'},
        ),
    ]