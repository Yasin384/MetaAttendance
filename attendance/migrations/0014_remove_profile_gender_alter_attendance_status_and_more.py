# Generated by Django 5.1.1 on 2024-10-05 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0013_alter_student_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='gender',
        ),
        migrations.AlterField(
            model_name='attendance',
            name='status',
            field=models.CharField(choices=[('present', 'Present'), ('late', 'Late'), ('absent', 'Absent')], max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.CharField(blank=True, choices=[('present', 'Present'), ('absent', 'Absent'), ('late', 'Late')], max_length=10),
        ),
    ]
