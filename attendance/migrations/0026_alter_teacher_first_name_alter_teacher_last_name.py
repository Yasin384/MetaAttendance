# Generated by Django 5.1.1 on 2024-10-08 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0025_attendance_duration_hours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='first_name',
            field=models.CharField(default='Unknown', max_length=200),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='last_name',
            field=models.CharField(default='Unknown', max_length=200),
        ),
    ]
