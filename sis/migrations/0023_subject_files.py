# Generated by Django 3.1.2 on 2020-10-14 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0022_auto_20201013_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='files',
            field=models.FileField(blank=True, upload_to='course/materials/'),
        ),
    ]
