# Generated by Django 5.1.1 on 2024-10-04 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0012_auto_20241005_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.CharField(blank=True, choices=[('present', 'Present'), ('absent', 'Absent'), ('late', 'Late')], max_length=20),
        ),
    ]
