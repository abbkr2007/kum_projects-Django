# Generated by Django 3.1.2 on 2020-11-29 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0039_auto_20201128_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='registration_No',
            field=models.CharField(blank=True, default='21906640182', max_length=11, null=True, unique=True),
        ),
    ]
